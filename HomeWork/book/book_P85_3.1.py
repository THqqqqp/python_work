"""
    求分段函数ReLu的值，ReLu(x)=
    {
        x, if x >= 0;
        0, if x < 0;
    }
"""


def ReLu(x):
    return max(x, 0)


if __name__ == "__main__":
    x = float(input("请输入一个实数："))
    print("ReLu(%f) = %f" % (x, ReLu(x)))
