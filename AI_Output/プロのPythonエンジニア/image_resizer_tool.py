import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import threading

def validate_file_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path {path} does not exist.")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"The path {path} is not a directory.")

def list_image_files(directory):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    return [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def resize_image(input_path, output_path, size, keep_aspect_ratio):
    with Image.open(input_path) as img:
        if keep_aspect_ratio:
            img.thumbnail(size)
        else:
            img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)

def create_output_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_images(input_dir, output_dir, size, keep_aspect_ratio, progress_callback, status_callback):
    try:
        validate_file_path(input_dir)
        create_output_directory(output_dir)
        image_files = list_image_files(input_dir)
        total_files = len(image_files)
        for i, file in enumerate(image_files):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            resize_image(input_path, output_path, size, keep_aspect_ratio)
            progress_callback((i + 1) / total_files)
        status_callback("処理が完了しました。")
    except Exception as e:
        status_callback(f"エラー: {str(e)}")

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("フリマ画像一括リサイズツール")
        self.root.geometry("600x400")

        self.input_dir = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.width = tk.StringVar(value="800")
        self.height = tk.StringVar(value="600")
        self.keep_aspect_ratio = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # ステップ1: ファイル選択
        frame1 = ttk.Frame(self.root, padding="10")
        frame1.pack(fill=tk.X)
        ttk.Label(frame1, text="入力フォルダ:").pack(side=tk.LEFT)
        ttk.Entry(frame1, textvariable=self.input_dir, width=40).pack(side=tk.LEFT)
        ttk.Button(frame1, text="選択", command=self.select_input_dir).pack(side=tk.LEFT)

        frame2 = ttk.Frame(self.root, padding="10")
        frame2.pack(fill=tk.X)
        ttk.Label(frame2, text="ファイルリスト:").pack(side=tk.TOP)
        self.file_listbox = tk.Listbox(frame2, height=5)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        # ステップ2: リサイズ設定
        frame3 = ttk.Frame(self.root, padding="10")
        frame3.pack(fill=tk.X)
        ttk.Label(frame3, text="リサイズ後の幅:").pack(side=tk.LEFT)
        ttk.Entry(frame3, textvariable=self.width, width=10).pack(side=tk.LEFT)
        ttk.Label(frame3, text="高さ:").pack(side=tk.LEFT)
        ttk.Entry(frame3, textvariable=self.height, width=10).pack(side=tk.LEFT)
        ttk.Checkbutton(frame3, text="アスペクト比を保持", variable=self.keep_aspect_ratio).pack(side=tk.LEFT)

        frame4 = ttk.Frame(self.root, padding="10")
        frame4.pack(fill=tk.X)
        ttk.Label(frame4, text="出力フォルダ:").pack(side=tk.LEFT)
        ttk.Entry(frame4, textvariable=self.output_dir, width=40).pack(side=tk.LEFT)
        ttk.Button(frame4, text="選択", command=self.select_output_dir).pack(side=tk.LEFT)

        # ステップ3: 実行と結果表示
        frame5 = ttk.Frame(self.root, padding="10")
        frame5.pack(fill=tk.X)
        ttk.Button(frame5, text="リサイズ開始", command=self.start_resizing).pack(side=tk.LEFT)

        self.progress = ttk.Progressbar(frame5, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(side=tk.LEFT, padx=10)

        self.status_label = ttk.Label(self.root, text="", padding="10")
        self.status_label.pack(fill=tk.X)

    def select_input_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.input_dir.set(selected_dir)
            self.update_file_list()

    def select_output_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.output_dir.set(selected_dir)

    def update_file_list(self):
        try:
            validate_file_path(self.input_dir.get())
            self.file_listbox.delete(0, tk.END)
            image_files = list_image_files(self.input_dir.get())
            for file in image_files:
                self.file_listbox.insert(tk.END, file)
        except Exception as e:
            messagebox.showerror("エラー", str(e))

    def start_resizing(self):
        try:
            width = int(self.width.get())
            height = int(self.height.get())
            if width <= 0 or height <= 0:
                raise ValueError("幅と高さは正の数値で入力してください。")
            input_dir = self.input_dir.get()
            output_dir = self.output_dir.get()
            size = (width, height)
            keep_aspect_ratio = self.keep_aspect_ratio.get()

            self.progress["value"] = 0
            self.status_label.config(text="リサイズ処理中...")

            threading.Thread(target=self.run_resizing, args=(input_dir, output_dir, size, keep_aspect_ratio)).start()
        except Exception as e:
            messagebox.showerror("エラー", str(e))

    def run_resizing(self, input_dir, output_dir, size, keep_aspect_ratio):
        def progress_callback(value):
            self.progress["value"] = value * 100

        def status_callback(message):
            self.status_label.config(text=message)

        process_images(input_dir, output_dir, size, keep_aspect_ratio, progress_callback, status_callback)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()