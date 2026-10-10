import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("時計アプリ")

clock_label = tk.Label(root, font=('Helvetica', 100))
clock_label.pack(pady=20)

update_time()

root.mainloop()