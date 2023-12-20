# 请定义一个book类，属性name、author、isbn、publisher、和price
# 方法：info()输出name、author、isbn、publisher、和price


class book:
    def __init__(self, name, author, isbn, publisher, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price

    def info(self):
        return f"书名:{self.name}\n作者:{self.author}\nisbn:{self.isbn}\n出版社:{self.publisher}\n价格:{self.price}"
