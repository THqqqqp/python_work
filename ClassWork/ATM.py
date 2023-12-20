"""
    ATM系统，要求：面向对象开发，控制台选择功能，有新增账号，查看账号，查看余额，取钱，存钱，登录等功能
"""




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def verify_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False


class ATM:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("登录成功！")
            return True
        else:
            print("登录失败！")
            return False

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"取款成功！当前余额为：{self.balance}")
        else:
            print("余额不足，取款失败！")

    def deposit(self, amount):
        self.balance += amount
        print(f"存款成功！当前余额为：{self.balance}")


def main():
    user_manager = UserManager()
    atm = ATM("admin", "123456")

    while True:
        print("请选择功能：1. 新增账号 2. 登录 3. 取款 4. 存款 5. 退出")
        choice = input()

        if choice == "1":
            username = input("请输入用户名：")
            password = input("请输入密码：")
            user_manager.add_user(username, password)
            print("新增账号成功！")
        elif choice == "2":
            username = input("请输入用户名：")
            password = input("请输入密码：")
            if atm.login(username, password):
                while True:
                    print("请选择功能：1. 取款 2. 存款 3. 退出")
                    choice = input()
                    if choice == "1":
                        amount = float(input("请输入取款金额："))
                        atm.withdraw(amount)
                    elif choice == "2":
                        amount = float(input("请输入存款金额："))
                        atm.deposit(amount)
                    elif choice == "3":
                        break
            else:
                print("登录失败！")
        elif choice == "3":
            amount = float(input("请输入取款金额："))
            atm.withdraw(amount)
        elif choice == "4":
            amount = float(input("请输入存款金额："))
            atm.deposit(amount)
        elif choice == "5":
            break
        else:
            print("输入有误，请重新输入！")


if __name__ == "__main__":
    main()
