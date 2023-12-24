"""
学生管理系统菜单类
"""


class MenuView:
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

    @staticmethod
    def get_choice():
        """
        获取用户选择
        """
        choice = input("请输入菜单选项：")
        return choice
