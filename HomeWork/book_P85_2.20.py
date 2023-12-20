"""
    已知元组 fruits = ('apple' ，'pear' ,'grapefruit' ,'pineapple','avocado') 元组中的元素个数;
    找出以'a' 开头的所有元素;输出每个元素及其对应的序号。
"""

t_fruits = ('apple', 'pear', 'grapefruit', 'pineapple', 'avocado')


def find_element(tuple, element):
    for index, item in enumerate(tuple):
        if item.startswith(element):
            print(item, index)


if __name__ == '__main__':
    find_element(t_fruits, input("请输入起始字符："))
