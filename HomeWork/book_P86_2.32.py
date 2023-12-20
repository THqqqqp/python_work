"""
    使用random.randint()函数生成1-100的随机整数，去掉重复的元素，
    然后按照从大到小的顺序进行排序。
"""
import random


def random_list():
    list1 = []
    for i in range(100):
        list1.append(random.randint(1, 100))
    return list1


def sort_list(list1):
    list1 = list(set(list1))
    list1.sort(reverse=True)
    print(list1)


if __name__ == "__main__":
    sort_list(random_list())
