class Book:
    def __init__(self, number=None, year=None, author=None, price=None):
        if type(number) == int and type(year) == int and type(author) == str and type(price) == float:
            self.__number = number
            self.__year = year
            self.__author = author
            self.__price = price
        elif number < 0 or year <= 1445:
            print('Invalid input: put number more than 0, year more than 1445.')
        elif isinstance(number, Book):
            self.__number = number.__number
            self.__year = number.__year
            self.__author = number.__author
            self.__price = number.__price
        elif number == year == author == price is None:
            self.__number = 0
            self.__year = 0
            self.__author = None
            self.__price = 0
        elif number > 0:
            self.__number = number
            self.__year = year
            self.__author = author
            self.__price = price


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

