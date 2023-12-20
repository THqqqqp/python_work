"""
用while循环解决鸡兔同笼问题，输入头和脚，输出鸡和兔的数量
"""


# 穷举法
def solve_chicken_rabbit(heads, feet):
    chickens = 0
    while chickens <= heads:
        rabbits = heads - chickens
        if (2 * chickens + 4 * rabbits) == feet:
            return chickens, rabbits
        chickens += 1
    return None


if __name__ == "__main__":
    heads = int(input("请输入头的数量："))
    feet = int(input("请输入脚的数量："))

    if solve_chicken_rabbit(heads, feet):
        chicken_nums, rabbit_nums = solve_chicken_rabbit(heads, feet)
        print("鸡的数量:", chicken_nums)
        print("兔子的数量:", rabbit_nums)
    else:
        print("无解")
