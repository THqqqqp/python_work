"""
    匹配以"www"起始且以".com"结尾的Web域名，例如，"www.baidu.com"
"""
import re

domains = input("请输入域名：")

regular = r"www\.(?P<Pojo>\w+)\.com"

matches = re.findall(regular, domains)

if matches:
    print("域名：", list(map(lambda x: 'www.'+x+'.com', matches)))
else:
    print("未找到域名")


