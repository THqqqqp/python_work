"""
学生管理系统表现层
"""
from Pojo.Student import Student
from Service.StudentService import StudentService
from Utils.ResultUtils import ResultUtils


class StudentView:
    def __init__(self):
        self.__student_service = StudentService()

    def get_all_students(self):
        """
        查询所有学生
        """
        if self.__student_service.get_all_students()['R'] == 'success':
            return self.__student_service.get_all_students()
        return self.__student_service.get_all_students()

    def get_student_by_name(self):
        """
        查询学生
        """
        student_name = input("请输入学生姓名：")
        return self.__student_service.get_student_by_name(student_name)

    def add_student(self):
        """
        添加学生
        :return Result
        """
        number = input("请输入学生学号：")
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        address = input("请输入学生地址：")
        sex = input("请输入学生性别：")
        phone = input("请输入学生电话：")
        student = Student(number, name, age, address, sex, phone)
        return self.__student_service.add_student(student)

    # todo：根据学号删除学生
    def delete_student_by_number(self):
        """
        删除学生
        """
        number = input("请输入学生学号：")
        return self.__student_service.delete_student_by_number(number)

    # todo：根据学生类，更新学生
    def update_student_by_number(self):
        """
        更新学生信息
        """
        number = int(input("请输入学生学号："))
        student = self.__student_service.get_student_by_number(number)
        print(student)
        if student['R'] == 'success':
            # 获取新的学生信息
            new_number = str(number)
            new_name = input("请输入新的学生姓名：")
            new_age = int(input("请输入新的学生年龄："))
            new_address = input("请输入新的学生地址：")
            new_sex = input("请输入新的学生性别：")
            new_phone = input("请输入新的学生电话：")
            new_student = Student(new_number, new_name, new_age, new_address, new_sex, new_phone)
            return self.__student_service.update_student(student, new_student)
        return ResultUtils.error("操作失败，不存在该学生")
