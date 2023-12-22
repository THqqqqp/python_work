"""
    向列表中逆向插入100个自然数，最后结果为：[100,99...1]
"""


def reverse_insert():
    result = []
    for i in range(100):
        result.insert(0, i+1)
    return result


if __name__ == "__main__":
    print(reverse_insert())