"""
学生管理系统表现层
"""
from Pojo.Student import Student
from Service.StudentService import StudentService


class StudentView:
    def __init__(self):
        self.__student_service = StudentService()

    @staticmethod
    def show_menu():
        """
        显示菜单
        """
        print("学生管理系统菜单:")
        print("1. 查询学生")
        print("2. 添加学生")
        print("3. 删除学生")
        print("4. 更新学生信息")
        print("5. 查询所有学生")
        print("0. 退出系统")

    def get_all_students(self):
        """
        查询所有学生
        """
        return self.__student_service.get_all_students()

    def get_student_by_name(self, name: str):
        """
        查询学生
        """
        return self.__student_service.get_student_by_name(name)

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
        return self.__student_service.add_student(student)['msg']

    # todo：根据学号删除学生
    def delete_student_by_number(self, number: str):
        """
        删除学生
        """
        return self.__student_service.delete_student_by_number(number)

    # todo：根据学生类，更新学生
    def update_student(self):
        """
        更新学生信息
        """
        name = input("请输入学生姓名：")
        student = self.__student_service.get_student_by_name(name)
        if student:
            # 获取新的学生信息
            new_name = input("请输入新的学生姓名：")
            new_age = int(input("请输入新的学生年龄："))
            new_address = input("请输入新的学生地址：")
            new_sex = input("请输入新的学生性别：")
            new_phone = input("请输入新的学生电话：")
            new_data = {
                "name": new_name,
                "age": new_age,
                "address": new_address,
                "sex": new_sex,
                "phone": new_phone
            }
            self.__student_service.update_student(student, new_data)
            print("学生信息更新成功")
        else:
            print("未找到该学生")

    def run(self):
        """
        运行学生管理系统
        """
        while True:
            self.show_menu()
            choice = input("请输入菜单选项：")
            if choice == "1":
                name = input("请输入学生姓名：")
                if self.get_student_by_name(name)['R'] == 'success':
                    for student in self.get_student_by_name(name)['obj']:
                        print(student)
                else:
                    print(self.get_student_by_name(name)['msg'])
            elif choice == "2":
                print(self.add_student())
            elif choice == "3":
                number = input("请输入学生学号：")
                print(self.delete_student_by_number(number)['msg'])
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                if self.get_all_students()['R'] == 'success':
                    for student in self.get_all_students()['obj']:
                        print(student, end='\n')
                else:
                    print(self.get_all_students()['msg'])
            elif choice == "0":
                print("退出系统")
                break
            else:
                print("无效选项，请重新输入")


if __name__ == '__main__':
    student_view = StudentView()
    student_view.run()
