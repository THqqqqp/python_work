"""
    用@property方法实现设置练习题数量和获取练习题数量
"""


class Book:
    """
    Book类，包含书名、作者、出版社、价格。"""

    def __init__(self, name, author, isbn, publisher, price):
        self._name = name
        self._author = author
        self._isbn = isbn
        self._publisher = publisher
        self._price = price

    def info(self):
        return "书名：%s\n作者：%s\nISBN：%s\n出版社：%s\n价格：%s" % (
            self._name, self._author, self._isbn, self._publisher, self._price)


class TextBook(Book):
    """
    TextBook类，从Book类继承。
    新增课件、练习题属性
    并重载info方法，输出所有属性"""

    def __init__(self, name, author, isbn, publisher, price, courseware, exercise):
        super().__init__(name, author, isbn, publisher, price)
        self._courseware = courseware
        self._exercise = exercise

    def info(self):
        return "书名：%s\n作者：%s\nISBN：%s\n出版社：%s\n价格：%s\n课件：%s\n练习题：%s" % (
            self._name, self._author, self._isbn, self._publisher, self._price, self._courseware, self._exercise)

    def set_courseware(self, courseware: int):
        """设置课件数量"""
        self._courseware = courseware

    def get_courseware(self):
        """获取课件数量"""
        return self._courseware

    @property
    def exercise(self):
        """获取练习题数量"""
        return self._exercise

    @exercise.setter
    def exercise(self, exercise: int):
        """设置练习题数量"""
        self._exercise = exercise


if __name__ == '__main__':
    book1 = Book("python入门", "李少", "123456", "光明出版社", "100")
    # print(book1.info())

    textBook1 = TextBook("python入门", "李少", "123456", "光明出版社", "100", 2, "练习题")
    print(textBook1.info())

    print("--------------------------")

    textBook1.exercise = 240
    print(textBook1.info())
