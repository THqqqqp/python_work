"""
    手机通讯录
    作出图形化界面，实现对通讯录的增删改查操作。
    点击联系人还可以查看具体信息
    每个联系人有以下字段：姓名，电话，邮箱，地址
"""

import tkinter as tk
from tkinter import messagebox

# 创建主窗口
window = tk.Tk()
window.title("手机通讯录")
window.geometry("400x500")

# 创建列表框用于显示联系人
contact_listbox = tk.Listbox(window, width=30)
contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

# 创建标签和文本框用于输入联系人信息
info_frame = tk.Frame(window)
info_frame.pack(side=tk.TOP, padx=10, pady=10)

name_label = tk.Label(info_frame, text="姓名:")
name_label.pack()
name_entry = tk.Entry(info_frame)
name_entry.pack()

phone_label = tk.Label(info_frame, text="电话:")
phone_label.pack()
phone_entry = tk.Entry(info_frame)
phone_entry.pack()

email_label = tk.Label(info_frame, text="邮箱:")
email_label.pack()
email_entry = tk.Entry(info_frame)
email_entry.pack()

address_label = tk.Label(info_frame, text="地址:")
address_label.pack()
address_entry = tk.Entry(info_frame)
address_entry.pack()

# 定义按钮点击事件
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contact_listbox.insert(tk.END, name)
    contact_listbox.itemconfig(tk.END, fg="blue")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contact_listbox.delete(selected_index)

def edit_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        contact_listbox.delete(selected_index)
        contact_listbox.insert(selected_index, name)
        contact_listbox.itemconfig(selected_index, fg="blue")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

def show_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        name = contact_listbox.get(selected_index)
        # 根据姓名获取联系人的其他信息，并显示在文本框中
        phone = "联系电话"
        email = "联系邮箱"
        address = "联系地址"
        messagebox.showinfo("联系人信息", f"姓名：{name}\n电话：{phone}\n邮箱：{email}\n地址：{address}")

# 创建按钮框架
button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, padx=10, pady=10)

# 创建按钮
add_button = tk.Button(button_frame, text="添加联系人", command=add_contact)
add_button.pack(side=tk.TOP, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="删除联系人", command=delete_contact)
delete_button.pack(side=tk.TOP, padx=5, pady=5)

edit_button = tk.Button(button_frame, text="编辑联系人", command=edit_contact)
edit_button.pack(side=tk.TOP, padx=5, pady=5)

show_button = tk.Button(button_frame, text="查看联系人", command=show_contact)
show_button.pack(side=tk.TOP, padx=5, pady=5)

# 运行主循环
window.mainloop()