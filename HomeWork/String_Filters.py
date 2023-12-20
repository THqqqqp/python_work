"""
    字符串过滤器，用户输入指定字符串，再输入一段文本，返回的文本就会过滤掉敏感词，变成***
"""


def get_keywords():
    sensitive_dict = {}
    while True:
        sensitive = input("请输入敏感词（输入'end'结束）：")
        if sensitive == 'end':
            break
        replace_word = input("请输入替换词：")
        sensitive_dict[sensitive.lower().strip()] = replace_word.strip()
    return sensitive_dict


def filter_text(text, sensitive_dict):
    # 替换敏感词
    for sensitive, replace_word in sensitive_dict.items():
        text = text.replace(sensitive, replace_word)
    print(text)


if __name__ == "__main__":
    sensitive_dict = get_keywords()
    text = input("请输入过滤前的文本:")
    filter_text(text, sensitive_dict)
