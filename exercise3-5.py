from __future__ import print_function
__author__ = 'ragomez'


class Point3D(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

if __name__ == '__main__':
    my_point = Point3D(x=1, y=2, z=3)
    print(my_point)
