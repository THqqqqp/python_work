# 嵌套if语句
bmi = 14
if bmi < 18.5:
    print('underweight')
else:
    if bmi >= 30:
        print('obese')
    elif 25 < bmi < 30:
        print('overweight')
    else:
        print('normal')

# and 连接条件语句
age = eval(input('请输入年龄:'))
if 70 > age > 18:
    print('True')

# or 连接条件语句
age = eval(input('请输入年龄：'))
if age < 18 or age > 60:
    print('False')

# 符合条件语句
num = eval(input('请输入一个数字：'))
# 判断值是否在0~3或者7~10之间
if (0 <= num <= 3) or (7 <= num <= 10):
    print('True')

# break语句
counter = 0
while counter < 10:
    counter += 1
    print(counter)
