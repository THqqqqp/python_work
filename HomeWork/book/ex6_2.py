# 请用book类 实例化 一个python_book对象，并调用info（）方法，输出信息

class book:
    def __init__(self, name, author, isbn, publisher, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price

    def info(self):
        return f"书名:{self.name}\n作者:{self.author}\nisbn:{self.isbn}\n出版社:{self.publisher}\n价格:{self.price}"


if __name__ == '__main__':
    # 测试
    python_book = book("example book", "example author", "123456789", "example publisher", 100)
    print(python_book.info())

