"""
    找出字符串“nice to meet you!”中字’t’的个数和位置。
"""


def count_t(str):
    count = 0
    idx = []
    for i in range(len(str)):
        if str[i] == "t":
            count += 1
            idx.append(i)
    return count, idx


if __name__ == "__main__":
    str = "nice to meet you!"
    print(count_t(str))