"""
列表工具类
"""


class ListUtils:
    @staticmethod
    def is_empty(lst):
        """
        判断列表是否为空
        :param lst: 列表
        :return: True || False
        """
        return len(lst) == 0
