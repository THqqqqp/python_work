"""
文件操作
"""

import os

# with open("files/hello.txt", 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         print(line, end='')

# 判断文件夹是否存在

directory = "files"
if os.path.exists(directory):
    for line in range(3):
        name = input("请输入姓名")
else:
    os.mkdir(directory)
    print("目录已创建")
