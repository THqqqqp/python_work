"""
    请将带扩展名的文件名“ssd_mobilenet.xml”分解为文件名和扩展名，分别保存在变量 fileName 和ext 上。
"""

fileName = "ssd_mobilenet.xml"

filename = fileName.split(".")[0]
ext = fileName.split(".")[1]

print("文件名：", filename, "扩展名：", ext)


