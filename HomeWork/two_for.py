"""
    将一个正整数解分解质因数,例如 输入70 输[2,5,7]
"""


def factor(n):
    result = []
    # 如果 n 等于 1，返回空列表
    if n == 1:
        return []
    # 从 2 开始循环，直到 i * i <= n
    i = 2
    while i * i <= n:
        # 如果 n 可以被 i 整除
        if n % i == 0:
            # 将 n 除以 i，并将 i 添加到结果列表中
            n //= i
            result.append(i)
        # 否则，i 加 1
        else:
            i += 1
    # 如果 n 大于 1，将 n 添加到结果列表中
    if n > 1:
        result.append(n)
    # 返回结果列表
    return result



if __name__ == "__main__":
    print(factor(70))
