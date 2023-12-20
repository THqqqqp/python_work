"""
输出10000-99999之间的所有回文数。
"""

# 常规解法
for num in range(10000, 100000):
    if (str(num)[0] == str(num)[-1]) and (str(num)[1] == str(num)[-2]):
        print(num)

# 字符串反转解法
for num in range(10000, 100000):
    if str(num) == str(num)[::-1]:
        print(num)


# 双指针解法 while
def is_palindrome_while(num):
    nums = str(num)
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True


# 双指针解法 for
def is_palindrome_for(num):
    nums = str(num)
    left, right = 0, len(nums) - 1
    for left in range(len(nums) // 2):
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    for num in range(10000, 100000):
        if is_palindrome_while(num):
            print(num)
        if is_palindrome_for(num):
            print(num)
