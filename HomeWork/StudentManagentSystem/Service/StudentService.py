"""
学生服务层
"""

from Pojo import Student
from Utils.ListUtils import ListUtils
from Utils.ResultUtils import ResultUtils


class StudentService:
    """
    学生服务层
    """

    def __init__(self):
        self.__student_list = []  # 用于存储学生数据的列表

    # todo：应当返回一个列表，包含学生对象
    def get_student_by_name(self, name: str):
        """
        根据学生姓名查询学生对象
        :param name: 姓名
        :return: student: 学生对象
        """
        if not ListUtils.is_empty(self.__student_list):
            return ResultUtils.success(list(filter(lambda student: student.name == name, self.__student_list)))
        return ResultUtils.error("没有找到该学生")

    def get_student_by_number(self, number: int):
        """
        根据学生学号查询学生对象
        :param number: 学号
        :return: student: 学生对象
        """
        if not ListUtils.is_empty(self.__student_list):
            for student in self.__student_list:
                if student.number == number:
                    return ResultUtils.success(student)
        return ResultUtils.error("没有找到该学生")

    def add_student(self, student: Student):
        """
        添加学生
        :param student: 学生对象
        """
        if self.get_student_by_number(student.number).get('R') == 'error':
            self.__student_list.append(student)
            return ResultUtils.success()
        else:
            return ResultUtils.error('已存在该学生')

    # def delete_student(self, student: Student):
    #     """
    #     删除学生
    #     :param student: 学生对象
    #     """
    #     self.students.remove(student)
    #
    # def update_student(self, student: Student, new_data: dict):
    #     """
    #     更新学生信息
    #     :param student: 学生对象
    #     :param new_data: 新的学生信息（字典格式）
    #     """
    #     # 更新学生对象的属性
    #     for key, value in new_data.items():
    #         setattr(student, key, value)
    #
    # def search_student_by_name(self, name: str):
    #     """
    #     根据姓名查询学生
    #     :param name: 姓名
    #     :return: 学生对象列表
    #     """
    #     result = []
    #     for student in self.students:
    #         if student.name == name:
    #             result.append(student)
    #     return result
    #
    def get_all_students(self):
        """
        获取所有学生
        :return: 学生对象列表
        """
        if ListUtils.is_empty(self.__student_list):
            return ResultUtils.error('暂无学生信息')
        return ResultUtils.success(self.__student_list)

    def delete_student_by_number(self, number: str):
        """
        根据学号删除学生
        :return: Result
        """
        if not ListUtils.is_empty(self.__student_list):
            for student in self.__student_list:
                if student.number == number:
                    self.__student_list.remove(student)
                    return ResultUtils.success()
                return ResultUtils.error('删除失败，不存在该学生')
        return ResultUtils.error('删除失败，不存在该学生')
