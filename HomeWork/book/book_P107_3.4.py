"""
猜数字游戏，用random.randint(1,100)生成随机整数，请用户输入整数。
若大了，输出“大了“
若小了，输出“小了“
若猜中，输出”猜中了“
"""

import random


def guess_number(guess_nums):
    number = random.randint(1, 101)
    if guess_nums:
        for i in range(guess_nums):
            print("第{0}次猜".format(i + 1))
            guess_Number = int(input("请输入一个1-100的整数:"))
            if guess_Number > number:
                print("\033[33m大了\033[0m")
            elif guess_Number < number:
                print("\033[33m小了\033[0m")
            else:
                print("\033[32m猜中了，共猜了{0}次\033[0m".format(i + 1))
                break
        print("\033[31m挑战失败，共挑战{0}\033[0m".format(guess_nums), "次")
        print("\033[31m正确答案:{0}\033[0m".format(number))
    else:
        i = 0
        while True:
            print("第{0}次猜".format(i + 1))
            i += 1
            guess_Number = int(input("请输入一个1-100的整数:"))
            if guess_Number > number:
                print("\033[33m大了\033[0m")
            elif guess_Number < number:
                print("\033[33m小了\033[0m")
            else:
                print("\033[32m猜中了，共猜了{0}次\033[0m".format(i + 1))
                break


def get_guess_nums():
    return int(input("请输入挑战次数，0表示无数次:"))


if __name__ == "__main__":
    guess_nums = get_guess_nums()
    guess_number(guess_nums)
