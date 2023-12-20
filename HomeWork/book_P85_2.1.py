"""
    题目2.1:请读者实现公里（km）和英里（mile）的转换（1mile=1.609344km）
"""


# 公里转英里
def km_to_mile(km):
    return km / 1.609344


# 英里转公里
def mile_to_km(mile):
    return mile * 1.609344


if __name__ == "__main__":
    km = int(input("请输入公里数："))
    print("{}公里= {}英里".format(km, km_to_mile(km)))
    mile = int(input("请输入英里数："))
    print("{}英里= {}公里".format(mile, mile_to_km(mile)))
