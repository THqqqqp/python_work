import tkinter as tk

def get_guess_nums():
    try:
        guess_nums = int(entry_guess_nums.get())
        if guess_nums <= 0:
            result_label.config(text="输入的挑战次数必须大于0")
            return None
        return guess_nums
    except ValueError:
        result_label.config(text="输入的挑战次数必须是一个整数")
        return None

def start_game():
    guess_nums = get_guess_nums()
    if guess_nums is None:
        return

    # 在这里添加你的游戏逻辑代码
    # ...

    # 更新结果
    result_label.config(text="你猜了{}次".format(guess_nums))

# 创建窗口
window = tk.Tk()
window.title("猜数字游戏")

# 创建输入框和结果标签
entry_guess_nums = tk.Entry(window, width=20)
entry_guess_nums.pack()

result_label = tk.Label(window, text="请输入挑战次数")
result_label.pack()

# 创建开始游戏按钮
start_button = tk.Button(window, text="开始游戏", command=start_game)
start_button.pack()

# 运行窗口主循环
window.mainloop()
