"""
封装返回类
"""


class ResultUtils:
    @staticmethod
    def success(obj=None, msg="操作成功"):
        """
        封装成功返回结果
        :param obj: 返回的对象或数据，默认为None
        :param msg: 返回的消息，默认为"操作成功"
        :return: 返回结果字典
        """
        result = {
            "R": "success",
            "obj": obj,
            "msg": msg
        }
        return result

    @staticmethod
    def error(msg="操作失败"):
        """
        封装错误返回结果
        :param msg: 返回的错误消息，默认为"操作失败"
        :return: 返回结果字典
        """
        result = {
            "R": "error",
            "msg": msg
        }
        return result
