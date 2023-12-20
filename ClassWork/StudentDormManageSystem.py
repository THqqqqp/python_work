"""
    学生宿舍管理系统
        1.添加学生宿舍
        2.删除学生宿舍
        3.修改学生宿舍
        4.查询学生宿舍
        5.退出系统
    面向对象，基于函数模块化开发
"""
from tabulate import tabulate


# 学生宿舍类
class StudentDorm:
    def __init__(self, dormId, dormStudents, isGood):
        self.dormId = dormId
        self.dormStudents = dormStudents
        self.isGood = isGood

    def displayInfo(self):
        header = ["寝室号", "学生", "是否优秀寝室"]
        data = [[self.dormId, ", ".join(self.dormStudents), self.isGood]]
        table_format = "pretty"
        print(tabulate(data, tablefmt=table_format))


def addDorm(dormId, dormStudents, isGood):
    # 全局变量
    # global studentDormList
    studentsList = dormStudents.split(" ")
    studentDormList.append(StudentDorm(dormId, studentsList, isGood))
    print("添加成功")
    # studentDormList[-1].displayInfo()


def selectDorms():
    if len(studentDormList) == 0:
        print("暂无数据")
    else:
        print("学生宿舍信息如下：")
        for i in range(len(studentDormList)):
            studentDormList[i].displayInfo()


def startSystem():
    print("-----欢迎使用学生宿舍管理系统------")
    print("系统功能：\n"
          "1.添加学生宿舍信息\n"
          "2.删除学生宿舍信息\n"
          "3.修改学生宿舍信息\n"
          "4.查看学生宿舍信息\n"
          "5.退出系统\n")
    while True:
        choice = input("请选择功能：")
        if choice == "1":
            addDorm(input("请输入宿舍号："), input("请输入宿舍学生（空格分割）："), input("请输入宿舍是否好："))
        elif choice == "4":
            selectDorms()
        elif choice == "5":
            print("退出系统")
            break
        else:
            print("无效的选择，请重新输入。\n")


if __name__ == "__main__":
    studentDormList = []
    startSystem()
