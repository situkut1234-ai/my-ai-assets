# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

class EmergencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("オンライン処理系のC言語開発|結合テストおよび性能試験|Linux環境|フルリモート")
        self.root.geometry("600x520")
        
        header = tk.Label(root, text="🚀 オンライン処理系のC言語開発|結合テストおよび性能試験|Linux環境|フルリモート", font=("Meiryo", 15, "bold"), fg="#2563EB")
        header.pack(pady=10)
        
        self.btn = tk.Button(root, text="✨ データを処理・生成する", font=("Meiryo", 12, "bold"), bg="#10B981", fg="white", command=self.run_process, padx=20, pady=10)
        self.btn.pack(pady=15)
        
        self.result_box = tk.Text(root, font=("Meiryo", 10), height=12)
        self.result_box.pack(fill="both", expand=True, padx=20, pady=10)
        self.result_box.insert("1.0", "【実行結果エリア】\n処理結果がここに表示されます。")
        
        self.status = tk.Label(root, text="準備完了", bd=1, relief="sunken", anchor="w")
        self.status.pack(side="bottom", fill="x")

    def run_process(self):
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert("1.0", "処理が正常に完了しました！")
        self.status.config(text="処理完了✨")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencyApp(root)
    root.mainloop()
