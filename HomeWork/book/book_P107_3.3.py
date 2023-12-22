"""
    题目3.3:输入“年份.月份”，输出该月份的天数。
"""


# Utils
def check_input(date):
    try:
        if len(date.split('.')) != 2:
            raise ValueError()
    except (ValueError, TypeError):
        print("输入的格式不正确，请输入：YYYY.MM")
        return False
    return True


# 方法1:
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_month_days(date):
    year, month = map(int, date.split('.'))
    if month in (1, 3, 5, 7, 8, 10, 12):
        print(31)
    elif month in (4, 6, 9, 11):
        print(30)
    elif month == 2:
        print(29) if is_leap_year(year) else print(28)


# 方法2:
from datetime import datetime


def get_month_days2(date):
    year, month = map(int, date.split('.'))
    print((datetime(year, month + 1, 1) - datetime(year, month, 1)).days)


if __name__ == "__main__":
    # 方法1
    while True:
        print("方法1:")
        date = input("请输入一个日期（格式：YYYY.MM）：")
        if check_input(date):
            get_month_days(date)
            break

    # 方法2
    while True:
        print("方法2:")
        date = input("请输入一个日期（格式：YYYY.MM）：")
        if check_input(date):
            get_month_days2(date)
            break
