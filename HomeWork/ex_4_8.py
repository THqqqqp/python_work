"""
    生成10个（1-10）的随机数字，然后从高到低排序并统计出现次数
"""
import collections
import random

numbers = [random.randint(1, 10) for i in range(1, 101)]
# print(sorted(numbers, reverse=True))
print(collections.Counter(numbers))


