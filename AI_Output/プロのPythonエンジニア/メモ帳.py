import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("メモ帳 - 新規")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
        root.title(f"メモ帳 - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"メモ帳 - {file_path}")

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"メモ帳 - {file_path}")

def exit_app():
    if messagebox.askokcancel("確認", "本当に終了しますか？"):
        root.destroy()

# ウィンドウの設定
root = tk.Tk()
root.title("メモ帳")

# メニューバーの設定
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# ファイルメニュー
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="新規", command=new_file)
file_menu.add_command(label="開く", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_command(label="保存して閉じる", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="終了", command=exit_app)

# テキストエリア
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# ウィンドウの表示
root.mainloop()