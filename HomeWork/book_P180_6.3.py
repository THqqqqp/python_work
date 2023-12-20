"""
    定义一个TextBook类，从Book类继承。
"""


class Book:
    """
    Book类，包含书名、作者、出版社、价格。"""

    def __init__(self, name, author, isbn, publisher, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price

    def info(self):
        return "书名：%s\n作者：%s\nISBN：%s\n出版社：%s\n价格：%s" % (
            self.name, self.author, self.isbn, self.publisher, self.price)


class TextBook(Book):
    """
    TextBook类，从Book类继承。
    新增课件、练习题属性"""

    def __init__(self, name, author, isbn, publisher, price, courseware, exercise):
        super().__init__(name, author, isbn, publisher, price)
        self.courseware = courseware
        self.exercise = exercise

    def __str__(self):
        return "书名：%s\n作者：%s\nISBN：%s\n出版社：%s\n价格：%s\n课件：%s\n练习题：%s" % (
            self.name, self.author, self.isbn, self.publisher, self.price, self.courseware, self.exercise)

    def info(self):
        print(self.__str__())


if __name__ == '__main__':
    book1 = Book("python入门", "李少", "123456", "光明出版社", "100")
    # print(book1.info())

    textBook1 = TextBook("python入门", "李少", "123456", "光明出版社", "100", "课件", "练习题")
    print(textBook1.__str__())
