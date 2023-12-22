"""
    删除列表中的重复元素
"""


def remove_repeat_element(list):
    result = []
    list = list.split(",")
    if not list:
        return list
    for i in list:
        if i not in result:
            result.append(i)
    print(result)


if __name__ == "__main__":
    remove_repeat_element(input("请输入列表："))
