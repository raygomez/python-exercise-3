from __future__ import print_function

__author__ = 'ragomez'

class MyClass(object):

    def __init__(self):
        self.value = ''

    def get_string(self):
        self.value = raw_input('Enter input:')

    def __str__(self):
        return self.value.upper()


if __name__=='__main__':
    obj = MyClass()
    obj.get_string()
    print(obj)