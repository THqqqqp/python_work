"""
    for循环输出斐波那契数列
"""


def fibonacci(n):
    result = []
    if n == 0:
        return result
    if n == 1:
        result.append(0)
        return result
    result.append(0)
    result.append(1)
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


if __name__ == "__main__":
    n = int(input("请输入要输出的斐波那契数列的长度："))
    print(fibonacci(n))
