"""
    随机生成100以内的自然数，随机选择加减乘除中的一种，
    让用户输入结果，系统判断结果是否正确
"""
import random


def generate_question():
    numbers = [random.randint(1, 100) for i in range(2)]
    operation = random.choice(['+', '-', '*', '/'])
    if operation == '+':
        answer = numbers[0] + numbers[1]
    elif operation == '-':
        answer = numbers[0] - numbers[1]
    elif operation == '*':
        answer = numbers[0] * numbers[1]
    else:
        # 特殊情况，被除数为0
        while numbers[1] == 0:
            numbers[1] = random.randint(1, 100)
        answer = numbers[0] / numbers[1]
    return numbers, operation, answer


def main():
    numbers, operation, answer = generate_question()
    print(f"{numbers[0]} {operation} {numbers[1]} = ?")
    user_answer = input("请输入答案：")
    if float(user_answer) == answer:
        print("回答正确！")
    else:
        print(f"回答错误，正确答案是：{answer}")


if __name__ == "__main__":
    main()
