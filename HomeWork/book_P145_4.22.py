"""
    用calendar模块实现闰年检测
"""
import calendar

y = int(input("请输入年份:"))
days = calendar.monthrange(y, 2)[1]
is_leap = days == 29
print("{}年2月有{}天，闰年：{}".format(y, days, is_leap))