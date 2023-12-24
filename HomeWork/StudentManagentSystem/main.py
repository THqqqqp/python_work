"""
    学生管理系统入口文件
"""
from View.StudentView import StudentView
from View.MenuView import MenuView


def run():
    student_view = StudentView()
    menu_view = MenuView()

    while True:
        menu_view.show_menu()
        choice = menu_view.get_choice()

        if choice == "1":
            # 查询学生代码
            # todo：需要重载用户输入，int为学号，str为姓名
            student_list = student_view.get_student_by_name()
            print(student_list)
        elif choice == "2":
            # 添加学生代码
            result = student_view.add_student()
            print(result['msg'])
        elif choice == "3":
            # 删除学生代码
            result = student_view.delete_student_by_number()
            print(result['msg'])
        elif choice == "4":
            # 更新学生信息代码
            result = student_view.update_student_by_number()
            print(result['msg'])
        elif choice == "5":
            # 查询所有学生代码
            result = student_view.get_all_students()
            if result['R'] == 'error':
                print(result['msg'])
            else:
                for student in result['obj']:
                    print(student)
        elif choice == "0":
            print("退出系统")
            break
        else:
            print("无效选项，请重新输入")
        print("所有学生：", student_view.get_all_students())


if __name__ == '__main__':
    run()
