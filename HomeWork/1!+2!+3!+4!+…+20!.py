"""
    求：1!+2!+3!+4!+…+20!
"""
from math import factorial

if __name__ == "__main__":
    sum = 0
    for i in range(1, 5):
        sum += factorial(i)
    print(sum)

    def digui(n):
        if n == 1:
            return 1
        else:
            return n+digui(n-1)
    '''
    传入5 返回 5+digui(4) 5+x
    传入4 返回 4+digui(3) 4+x
    传入3 返回 3+digui(2) 3+x
    传入2 返回 2+digui(1) 2+x
    传入1 返回 1          1
    '''
    print(digui(5))
    print(1)