"""
    已知列表['h','e','l','l','o']，要求转换为字符串
"""


def list_to_string(list):
    return ''.join(list)


if __name__ == '__main__':
    str_list = ['h', 'e', 'l', 'l', 'o']
    print(list_to_string(str_list))
