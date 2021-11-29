import math
from abc import abstractmethod
from math import sqrt


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Figure:
    @abstractmethod
    def area(self):
        raise NotImplemented

    @abstractmethod
    def perimeter(self):
        raise NotImplemented


class Circle(Point, Figure):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self._r = r

    def area(self):
        return math.pi * (self._r * self._r)

    def perimeter(self):
        return 2 * math.pi * self._r


class Triangle(Point, Figure):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    def perimeter(self):
        return self._z + self._x + self._y

    def area(self):
        p = self.perimeter() // 2
        return sqrt(p * (p - self._x) * (p - self._y) * (p - self._z))


class Square(Point, Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return (self._x + self._y) ** 2

    def perimeter(self):
        return (self._x + self._y) * 4
