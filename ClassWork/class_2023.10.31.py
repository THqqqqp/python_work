"""
生成1-100以内的素数
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(1, 101):
        if is_prime(i):
            print(i)
