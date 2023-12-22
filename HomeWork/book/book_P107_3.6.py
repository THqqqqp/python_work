"""
找出100以内能被3或7整除，但不能同时被3和7整除的数
"""

# while解法
if __name__ == "__main__":
    result = []
    i = 0
    while i <= 100:
        if i % 3 == 0 or i % 7 == 0:
            result.append(i)
        if i % 3 == 0 and i % 7 == 0:
            result.remove(i)
        i += 1
    print("(while)100以内能被3或7整除，但不能同时被3和7整除的数:", result)


# for解法
if __name__ == "__main__":
    result = []
    for i in range(101):
        if i % 3 == 0 or i % 7 == 0:
            result.append(i)
        elif i % 3 == 0 and i % 7 == 0:
            result.remove(i)
    print("(for)100以内能被3或7整除，但不能同时被3和7整除的数:", result)
