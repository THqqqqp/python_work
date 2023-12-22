"""
输出99乘法表
"""

# while解法
if __name__ == "__main__":
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print(j, "*", i, "=", i * j, end="\t")
            j += 1
        print()
        i += 1

# for解法
if __name__ == "__main__":
    i = 1
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "*", i, "=", i * j, end="\t")
        print()
