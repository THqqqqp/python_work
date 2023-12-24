"""
数字工具类
"""

import re


def is_number(value):
    if re.match(r'^[0-9]+(\.[0-9]+)?$', value):
        return True
    return False
