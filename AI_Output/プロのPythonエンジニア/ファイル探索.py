import tkinter as tk
import os

# AI_Outputフォルダとその中のフォルダを再帰的に探索
def find_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

# ルートディレクトリを指定（AI_Outputフォルダ）
root_directory = 'AI_Output'

# .pyファイルを探索
py_files = find_py_files(root_directory)

# ファイル名一覧を取得
file_names = [os.path.basename(file) for file in py_files]

# ウィンドウの設定
root = tk.Tk()
root.title("社内ポータル")

# メニューバーの設定
menu = tk.Menu(root)
root.config(menu=menu)

# メニューの追加
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="ファイル", menu=file_menu)
for file in file_names:
    file_menu.add_command(label=file, command=lambda file=file: exec(open(file).read()))

# ファイルのラベル
label = tk.Label(root, text="ようこそ！社内ポータルへ", font=("Helvetica", 24))
label.pack(pady=20)

# ウィンドウの表示
root.mainloop()