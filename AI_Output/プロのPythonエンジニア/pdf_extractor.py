import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
from tkinter.ttk import Label, Button, Text

class PDFExtractor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Extractor 🚀")
        self.geometry("400x300")
        
        self.pdf_path = tk.StringVar()
        self.extracted_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # 条件を選ぶ/入力
        Label(self, text="PDFファイルを選択してください", font=('Helvetica', 12)).pack(pady=10)
        Button(self, text="📁 ファイル選択", command=self.select_file).pack(pady=5)
        
        # 実行ボタンを押す
        Button(self, text="🚀 抽出実行", command=self.extract_text, width=20).pack(pady=20)
        
        # 結果を見る/コピー
        Label(self, text="抽出したテキスト:", font=('Helvetica', 12)).pack(pady=5)
        self.result_textbox = Text(self, height=10, width=40, wrap="word")
        self.result_textbox.pack(pady=5)
        
        Button(self, text="📋 コピー", command=self.copy_to_clipboard).pack(pady=10)
        
        # ステータスバー
        self.status_bar = Label(self, text="準備完了", font=('Helvetica', 10))
        self.status_bar.pack(side="bottom", fill="x", pady=5)
    
    def select_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if file_path:
                self.pdf_path.set(file_path)
                self.status_bar.config(text="ファイル選択完了: " + file_path)
        except Exception as e:
            messagebox.showerror("エラー", f"ファイル選択中にエラーが発生しました。\n{str(e)}")
            self.status_bar.config(text="エラー: ファイル選択失敗")
    
    def extract_text(self):
        if not self.pdf_path.get():
            messagebox.showwarning("警告", "PDFファイルを選択してください。")
            self.status_bar.config(text="警告: PDFファイル未選択")
            return
        
        try:
            with open(self.pdf_path.get(), "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                self.extracted_text.set(text)
                self.result_textbox.delete("1.0", tk.END)
                self.result_textbox.insert(tk.END, text)
                self.status_bar.config(text="テキスト抽出完了")
        except Exception as e:
            messagebox.showerror("エラー", f"テキスト抽出中にエラーが発生しました。\n{str(e)}")
            self.status_bar.config(text="エラー: テキスト抽出失敗")
    
    def copy_to_clipboard(self):
        if not self.extracted_text.get():
            messagebox.showwarning("警告", "抽出したテキストがありません。")
            self.status_bar.config(text="警告: 抽出したテキストなし")
            return
        
        try:
            self.clipboard_clear()
            self.clipboard_append(self.extracted_text.get())
            messagebox.showinfo("情報", "テキストがクリップボードにコピーされました。")
            self.status_bar.config(text="クリップボードにコピー完了")
        except Exception as e:
            messagebox.showerror("エラー", f"クリップボードへのコピー中にエラーが発生しました。\n{str(e)}")
            self.status_bar.config(text="エラー: クリップボードコピー失敗")

if __name__ == "__main__":
    app = PDFExtractor()
    app.mainloop()