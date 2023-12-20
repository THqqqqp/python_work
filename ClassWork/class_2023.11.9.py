"""
用*画图， 画直角三角形，等腰三角形，边长由用户输入
"""


# 左直角三角形
def draw_left_triangle(side_length):
    for i in range(1, side_length + 1):
        print('*' * i)


# 右直角三角形
def draw_right_triangle(side_length):
    for i in range(1, side_length + 1):
        print(' ' * (side_length - i) + '*' * i)


# 左倒直角三角形
def draw_upside_down_left_triangle(side_length):
    for i in range(1, side_length + 1):
        print('*' * side_length, end="" + "\n")
        side_length -= 1


# 左倒右直角三角形
def draw_upside_down_right_triangle(side_length):
    for i in range(1, side_length + 1):
        # print(" " * side_length+)


# 等腰三角形
def draw_isosceles_triangle(side_length):
    for i in range(1, side_length + 1):
        spaces = ' ' * (side_length - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# 倒等腰三角形
def draw_upside_down_isosceles_triangle(side_length):
    for i in range(side_length, 0, -1):
        spaces = ' ' * (side_length - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# 画菱形
def draw_rhombus(side_length):
    draw_isosceles_triangle(side_length)
    draw_upside_down_isosceles_triangle(side_length)


# 获取用户输入
side_length = int(input("请输入底边边长："))

print("等腰三角形：")
draw_isosceles_triangle(side_length)

print("倒等腰三角形：")
draw_upside_down_isosceles_triangle(side_length)

print("菱形：")
draw_rhombus(side_length)

print("左直角三角形：")
draw_left_triangle(side_length)

print("右直角三角形：")
draw_right_triangle(side_length)

print("倒左直角三角形：")
draw_upside_down_left_triangle(side_length)

print("倒右直角三角形：")
draw_upside_down_right_triangle(side_length)
