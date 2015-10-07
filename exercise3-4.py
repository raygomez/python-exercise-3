from __future__ import print_function
__author__ = 'ragomez'


class Person(object):

    def get_gender(self):
        raise NotImplementedError('Missing implementation')


class Male(Person):

    def get_gender(self):
        return "Male"


class Female(Person):

    def get_gender(self):
        return "Female"

if __name__ == '__main__':

    male = Male()
    female = Female()

    print(male.get_gender())
    print(female.get_gender())
