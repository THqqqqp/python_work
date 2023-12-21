"""
学生实体类
"""


class Student:
    """
    学生实体类
    :param number: 学号
    :param name: 姓名
    :param age: 年龄
    :param address: 地址
    :param sex: 性别
    :param phone: 电话
    """

    def __init__(self, number: str, name: str, age: int, address: str, sex: str, phone: str):
        self.__number = number
        self.__name = name
        self.__age = age
        self.__address = address
        self.__sex = sex
        self.__phone = phone

    def __str__(self):
        return "学号：{0}, 姓名: {1}, 年龄: {2}, 地址: {3}, 性别: {4}, 电话: {5}".format(
            self.__number, self.__name, self.__age, self.__address, self.__sex, self.__phone
        )

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value
