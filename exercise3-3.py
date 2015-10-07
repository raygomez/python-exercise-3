from __future__ import print_function
__author__ = 'ragomez'


class Shape(object):

    def get_area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

if __name__ == '__main__':

    square = Square(length=10)
    print(square.get_area())

    shape = Shape()
    print(shape.get_area())
