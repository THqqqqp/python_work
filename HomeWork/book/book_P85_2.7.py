"""
    已知变量    name ='Xiaoming'，height= 179.8，weight= 75.0，
    请格式化输出 name: Xiaoming; Height: 179. 8cm ; Weight : 75. 0kg"。
"""


def format_name(name, height, weight):
    return "Name: {0}; Height: {1}cm ; Weight : {2}kg".format(name, height, weight)


if __name__ == "__main__":
    print(format_name("Xiaoming", 179.8, 75.0))
