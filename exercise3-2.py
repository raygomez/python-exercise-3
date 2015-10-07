from __future__ import print_function
import math
__author__ = 'ragomez'


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

if __name__=='__main__':
    circle = Circle(radius=10)
    print(circle.getArea())
