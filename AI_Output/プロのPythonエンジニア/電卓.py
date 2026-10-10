import tkinter as tk

# ウィンドウの設定
root = tk.Tk()
root.title("電卓")

# 入力フィールド
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ボタンクリック時の動作
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))

# ボタンの作成と配置
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('+', 4, 1), ('=', 4, 2),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2,
                       command=lambda t=text: button_click(t) if t in '0123456789' else ('C' if t == 'C' else '+='))
    button.grid(row=row, column=col)

# ウィンドウの表示
root.mainloop()