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
                if int(student.number) == int(number):
                    return ResultUtils.success(student)
            return ResultUtils.error("没有找到该学生")
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

    def update_student(self, student, new_student: Student):
        """
        更新学生信息
        :param student:
        :param new_student:
        :return:
        """
        if not ListUtils.is_empty(self.__student_list):
            for index, s in enumerate(self.__student_list):
                if int(s.number) == int(new_student.number):
                    # 这里把student替换成new_student
                    print("number相等，进行替换")
                    s.name = new_student.name
                    s.sex = new_student.sex
                    s.age = new_student.age
                    s.address = new_student.address
                    s.phone = new_student.phone
                    return ResultUtils.success(s, "更新成功")
            return ResultUtils.error("更新失败，不存在该学生")
        return ResultUtils.error("更新失败，不存在该学生")
