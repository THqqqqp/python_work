"""
根据年份和月份判断一个月有多少天
@param year: 年份
@param month: 月份
@return: 返回一个月有多少天
"""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_month_days(date):
    year, month = map(int, date.split('.'))
    if month in (1, 3, 5, 7, 9, 11):
        return 31
    elif month in (4, 6, 8, 10, 12):
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28


if __name__ == "__main__":
    while True:
        date = input("请输入一个日期（格式：YYYY.MM）：")
        try:
            year, month = map(int, date.split('.'))
            if len(date.split('.')) != 2:
                raise ValueError("输入的格式不正确，请输入：YYYY.MM")
            days = get_month_days(date)
            print(f"{date}有 {days} 天。")
            break
        except ValueError as e:
            print("输入的格式不正确，请输入：YYYY.MM")
