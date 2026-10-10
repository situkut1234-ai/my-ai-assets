import customtkinter as ctk
from tkinter import messagebox
import os
import subprocess
import zipfile

# デザインテーマ設定（ダークモード＆ブルーアクセント）
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def launch_app(filepath):
    try:
        subprocess.Popen(["python", filepath])
    except Exception as e:
        messagebox.showerror("エラー", f"起動に失敗しました:\n{e}")

def package_app(filepath, app_name):
    try:
        package_dir = os.path.join(BASE_DIR, "商品パッケージ", app_name)
        os.makedirs(package_dir, exist_ok=True)
        
        # 1. 綺麗にフォーマットされた取扱説明書
        readme_path = os.path.join(package_dir, "取扱説明書.txt")
        with open(readme_path, "w", encoding="utf-8-sig") as f:
            f.write(f"==================================================\n")
            f.write(f"  {app_name} - 取扱説明書 & マニュアル\n")
            f.write(f"==================================================\n\n")
            f.write(f"【概要】\n本ツールは快適な作業効率化を提供するデスクトップアプリケーションです。\n\n")
            f.write(f"【使用方法】\n1. Python環境で {app_name}.py を実行してください。\n")
            f.write(f"2. 必要なライブラリがある場合は `pip install` で追加してください。\n")

        # 2. PR文作成
        pr_path = os.path.join(package_dir, "販売用PR文_ココナラ・note用.txt")
        with open(pr_path, "w", encoding="utf-8-sig") as f:
            f.write(f"【タイトル】\n【洗練されたUI/高機能】{app_name} 業務効率化ツール\n\n")
            f.write(f"【商品説明文】\nご覧いただきありがとうございます！\n")
            f.write(f"日々の面倒な作業を一瞬で解決する『{app_name}』の完成版ツールです。\n\n")
            f.write(f"■ 本商品の特徴\n・直感的に操作できる洗練されたモダンUIデザイン\n・ボタン一つで正確な自動処理を実行\n\n")

        # 3. ZIPファイル作成
        zip_path = os.path.join(package_dir, f"{app_name}_納品用データ.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(filepath, arcname=f"{app_name}.py")
            zipf.write(readme_path, arcname="取扱説明書.txt")

        subprocess.Popen(["python", "worker.py", "プロのセールスコピーライター", f"「{app_name}」を魅力的にアピールする最高品質の販売用商品説明文"])

        os.startfile(package_dir)
        messagebox.showinfo("商品化完了", f"『{app_name}』の商品パッケージ（ZIP・説明書・PR文）を作成しました！")

    except Exception as e:
        messagebox.showerror("エラー", f"商品パッケージ作成エラー:\n{e}")

class ModernPortalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Development Studio - Portal")
        self.geometry("680x600")
        self.configure(fg_color="#1A1A24")

        # ヘッダー領域
        self.header_frame = ctk.CTkFrame(self, fg_color="#242432", corner_radius=15)
        self.header_frame.pack(fill="x", padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="🏢 AI Agent Studio - Portal", 
            font=ctk.CTkFont(family="Meiryo", size=20, weight="bold"),
            text_color="#F9FAFB"
        )
        self.title_label.pack(side="left", padx=20, pady=15)

        self.refresh_btn = ctk.CTkButton(
            self.header_frame, 
            text="🔄 更新", 
            width=80,
            command=self.refresh_apps,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=ctk.CTkFont(family="Meiryo", size=12, weight="bold")
        )
        self.refresh_btn.pack(side="right", padx=20, pady=15)

        # アプリ一覧スクロールエリア
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.refresh_apps()

    def refresh_apps(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        found_apps = False
        
        for root_dir, dirs, files in os.walk(BASE_DIR):
            for file in files:
                if file.endswith(".py") and file != "社内ポータル.py":
                    found_apps = True
                    filepath = os.path.join(root_dir, file)
                    app_name = file.replace(".py", "")

                    # カードデザイン枠
                    card = ctk.CTkFrame(self.scroll_frame, fg_color="#2B2B3C", corner_radius=12)
                    card.pack(fill="x", pady=6, padx=5)

                    # アプリ名
                    app_label = ctk.CTkLabel(
                        card, 
                        text=f"💻 {app_name}", 
                        font=ctk.CTkFont(family="Meiryo", size=14, weight="bold"),
                        text_color="#E5E7EB"
                    )
                    app_label.pack(side="left", padx=15, pady=12)

                    # ボタン群
                    btn_pack = ctk.CTkButton(
                        card, 
                        text="📦 商品化", 
                        width=90,
                        fg_color="#EAB308",
                        hover_color="#CA8A04",
                        text_color="#1E1E2E",
                        font=ctk.CTkFont(family="Meiryo", size=12, weight="bold"),
                        command=lambda p=filepath, n=app_name: package_app(p, n)
                    )
                    btn_pack.pack(side="right", padx=(5, 15), pady=12)

                    btn_launch = ctk.CTkButton(
                        card, 
                        text="▶ 起動", 
                        width=80,
                        fg_color="#10B981",
                        hover_color="#059669",
                        font=ctk.CTkFont(family="Meiryo", size=12, weight="bold"),
                        command=lambda p=filepath: launch_app(p)
                    )
                    btn_launch.pack(side="right", padx=5, pady=12)

        if not found_apps:
            lbl = ctk.CTkLabel(
                self.scroll_frame, 
                text="作成されたアプリがまだありません。\nAIにアプリの開発を依頼してみましょう！", 
                font=ctk.CTkFont(family="Meiryo", size=14),
                text_color="#9CA3AF"
            )
            lbl.pack(pady=40)

if __name__ == "__main__":
    app = ModernPortalApp()
    app.mainloop()