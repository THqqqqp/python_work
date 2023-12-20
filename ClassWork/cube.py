"""
    2023028107 李明睿
    神奇魔方阵，n行n列，由自然数1～n*n组成的方阵。该方阵中的数符合以下规律：
        1.方阵中的每个元素都不相等。
        2.每行、每列以及两条对角线的和都相等。
    求一个5*5的魔方阵。
"""
import numpy as np
# 定义魔方阵的大小
n = 5
# 创建一个全为0的矩阵
matrix = np.zeros((n, n), dtype=int)
# 计算每行每列的和
s = n * (n ** 2 + 1) // 2
# 初始位置为第一行中间
i, j = 0, n // 2
# 生成魔方阵
for k in range(1, n ** 2 + 1):
    matrix[i][j] = k
    # 下一个位置
    ni = (i - 1) % n
    nj = (j + 1) % n
    # 若下一个位置已经填有数字，则往下一行填
    if matrix[ni][nj]:
        i = (i + 1) % n
    else:
        i, j = ni, nj
    # 输出魔方阵
    for row in matrix:
        print('\t'.join([str(x) for x in row]))
    print("------------------")
print(f"\n每行、每列、主对角线、副对角线的和均为{s}")
