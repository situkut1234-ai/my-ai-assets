import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import logging

# ログ設定
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# アスペクト比を維持しながらリサイズ
def resize_image(image, size, keep_aspect_ratio):
    if keep_aspect_ratio:
        width_percent = (size[0] / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(width_percent)))
        return image.resize((size[0], hsize), Image.LANCZOS)
    else:
        return image.resize(size, Image.LANCZOS)

# ファイル選択ダイアログを開く
def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    file_list.delete(0, tk.END)
    for file_path in file_paths:
        file_list.insert(tk.END, file_path)

# リサイズ処理
def resize_images():
    try:
        output_dir = filedialog.askdirectory()
        if not output_dir:
            messagebox.showwarning("警告", "保存先ディレクトリを選択してください。")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        width = int(width_entry.get())
        height = int(height_entry.get())
        size = (width, height)
        keep_aspect_ratio = aspect_ratio_var.get()

        total_files = file_list.size()
        progress['maximum'] = total_files
        progress['value'] = 0

        for i in range(total_files):
            file_path = file_list.get(i)
            try:
                with Image.open(file_path) as img:
                    resized_img = resize_image(img, size, keep_aspect_ratio)
                    file_name = os.path.basename(file_path)
                    output_path = os.path.join(output_dir, file_name)
                    resized_img.save(output_path)
            except Exception as e:
                logging.error(f"Error processing file {file_path}: {e}")
                messagebox.showerror("エラー", f"ファイル {file_path} の処理中にエラーが発生しました。詳細はログファイルを確認してください。")
                continue
            progress['value'] += 1
            root.update_idletasks()

        messagebox.showinfo("完了", "リサイズ処理が完了しました。")
    except ValueError:
        messagebox.showerror("エラー", "幅と高さには数値を入力してください。")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        messagebox.showerror("エラー", "予期せぬエラーが発生しました。詳細はログファイルを確認してください。")

# メインウィンドウの設定
root = tk.Tk()
root.title("フリマ画像一括リサイズツール")
root.geometry("600x400")
root.configure(bg="#1E1E2E")

# カスタムTkinterを使用するための設定
try:
    import customtkinter as ctk
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.title("フリマ画像一括リサイズツール")
    root.geometry("600x400")
    root.configure(bg="#1E1E2E")
except ImportError:
    messagebox.showwarning("警告", "customtkinterがインストールされていません。標準のTkinterを使用します。")

# ファイル選択ボタン
select_button = ctk.CTkButton(root, text="画像ファイルを選択", command=select_files, fg_color="#3B82F6", text_color="white", corner_radius=10, font=("Helvetica", 14))
select_button.pack(pady=10)

# 選択されたファイルリスト
file_list = tk.Listbox(root, bg="#333", fg="white", selectmode=tk.MULTIPLE, height=10, width=60)
file_list.pack(pady=10)

# リサイズ設定
setting_frame = ctk.CTkFrame(root, fg_color="#1E1E2E", corner_radius=10)
setting_frame.pack(pady=10)

width_label = ctk.CTkLabel(setting_frame, text="リサイズ後の幅:", fg_color="#1E1E2E", text_color="white", font=("Helvetica", 12))
width_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")

width_entry = ctk.CTkEntry(setting_frame, width=100)
width_entry.grid(row=0, column=1, padx=15, pady=10)

height_label = ctk.CTkLabel(setting_frame, text="リサイズ後の高さ:", fg_color="#1E1E2E", text_color="white", font=("Helvetica", 12))
height_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")

height_entry = ctk.CTkEntry(setting_frame, width=100)
height_entry.grid(row=1, column=1, padx=15, pady=10)

aspect_ratio_var = tk.BooleanVar()
aspect_ratio_check = ctk.CTkCheckBox(setting_frame, text="アスペクト比を維持", variable=aspect_ratio_var, fg_color="#3B82F6", text_color="white", font=("Helvetica", 12))
aspect_ratio_check.grid(row=2, column=0, columnspan=2, padx=15, pady=10)

# リサイズ開始ボタン
resize_button = ctk.CTkButton(root, text="リサイズ開始", command=resize_images, fg_color="#10B981", text_color="white", corner_radius=10, font=("Helvetica", 14))
resize_button.pack(pady=10)

# プログレスバー
progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress.pack(pady=10)

root.mainloop()