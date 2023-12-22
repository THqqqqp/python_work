class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            print("联系人已存在，无法添加。")
        else:
            self.contacts[name] = phone_number
            print("联系人添加成功。")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("联系人删除成功。")
        else:
            print("联系人不存在，无法删除。")

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            print("联系人更新成功。")
        else:
            print("联系人不存在，无法更新。")

    def search_contact(self, name):
        if name in self.contacts:
            phone_number = self.contacts[name]
            print(f"联系人：{name}，电话号码：{phone_number}")
        else:
            print("联系人不存在。")

    def display_all_contacts(self):
        if self.contacts:
            print("所有联系人：")
            for name, phone_number in self.contacts.items():
                print(f"联系人：{name}，电话号码：{phone_number}")
        else:
            print("通讯录为空。")


def main():
    address_book = AddressBook()

    while True:
        print("请选择功能：1. 添加联系人 2. 删除联系人 3. 更新联系人 4. 查询联系人 5. 查询所有联系人 6. 退出")
        choice = input()

        if choice == "1":
            name = input("请输入联系人姓名：")
            phone_number = input("请输入联系人电话号码：")
            address_book.add_contact(name, phone_number)
        elif choice == "2":
            name = input("请输入联系人姓名：")
            address_book.delete_contact(name)
        elif choice == "3":
            name = input("请输入联系人姓名：")
            new_phone_number = input("请输入新的电话号码：")
            address_book.update_contact(name, new_phone_number)
        elif choice == "4":
            name = input("请输入联系人姓名：")
            address_book.search_contact(name)
        elif choice == "5":
            address_book.display_all_contacts()
        elif choice == "6":
            break
        else:
            print("输入有误，请重新输入！")


if __name__ == "__main__":
    main()
