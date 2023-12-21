"""
    通讯录
    面向对象
"""


class Contact:
    """
    联系人类
    :param  name: 姓名
    :param  phone: 电话
    :param  address: 地址
    """

    def __init__(self, name: str, phone: str, address: str):
        self.__name = name
        self.__phone = phone
        self.__address = address

    def __str__(self):
        return "姓名: {}, 电话: {}, 地址: {}".format(self.__name, self.__phone, self.__address)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

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


class AddressBook:
    """
    通讯录类
    :param __contact_list: 联系人列表
    """

    def __init__(self):
        self.__contact_list = []

    def add_contactList(self, contact: Contact):
        """
        添加联系人
        :param contact: 联系人
        :return:
        """
        if self.isExist_name(contact.name):
            print("该联系人已存在")
        else:
            self.__contact_list.append(contact)
            print("添加成功")

    def show_contactList(self):
        """
        显示联系人列表
        :return: contact_list
        """
        if len(self.__contact_list) != 0:
            for contact in self.__contact_list:
                print(contact)

    def isExist_name(self, name: str):
        """
        判断是否存在该联系人
        :param name: 联系人姓名
        :return: 是否存在
        """
        if len(self.__contact_list) != 0:
            for contact in self.__contact_list:
                if contact.name == name:
                    return True
        else:
            return False


if __name__ == '__main__':
    contact1 = Contact("张三", "13800000000", "北京")
    contact2 = Contact("李四", "13800000000", "浙江")
    addressBook = AddressBook()
    addressBook.add_contactList(contact1)
    addressBook.add_contactList(contact2)
    addressBook.show_contactList()
