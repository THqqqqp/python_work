"""
    青春有你
    接受选手的姓名和票数，输出排序后的成绩
    作出图形化界面
"""

import tkinter as tk
from operator import itemgetter

# 定义一个空列表用于存储选手姓名和票数
scores = []

# 创建主窗口
window = tk.Tk()
window.title("选手成绩排序")
window.geometry("300x400")

# 创建标签和文本框用于输入选手姓名和票数
name_label = tk.Label(window, text="姓名:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

score_label = tk.Label(window, text="票数:")
score_label.pack()
score_entry = tk.Entry(window)
score_entry.pack()


# 定义按钮点击事件
def add_score():
    name = name_entry.get()
    score = int(score_entry.get())
    scores.append((name, score))
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)


def show_scores():
    sorted_scores = sorted(scores, key=itemgetter(1), reverse=True)
    result_text = "\n".join(f"{name}: {score}" for name, score in sorted_scores)
    result_label.configure(text=result_text)


# 创建按钮
add_button = tk.Button(window, text="添加成绩", command=add_score)
add_button.pack()

show_button = tk.Button(window, text="显示成绩", command=show_scores)
show_button.pack()

# 创建标签用于显示排序后的成绩
result_label = tk.Label(window, text="")
result_label.pack()

# 运行主循环
window.mainloop()
