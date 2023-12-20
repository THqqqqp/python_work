"""
    定义一个TextBook类，从Book类继承。
"""


class Book:
    def __init__(self, name, author, isbn, publisher, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price

    def info(self):
        return "书名：%s\n作者：%s\nISBN：%s\n出版社：%s\n价格：%s" % (
        self.name, self.author, self.isbn, self.publisher, self.price)

if __name__ == '__main__':
    book1 = Book("python入门", "李少", "123456", "光明出版社", "100")
    print(book1.info())