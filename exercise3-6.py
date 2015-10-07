from __future__ import print_function
__author__ = 'ragomez'


class Car(object):

    def __init__(self, brand='', max_speed=0):
        self.brand = brand
        self.max_speed = max_speed

    def set_brand(self, brand):
        self.brand = brand

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def print_data(self):
        print('Car(brand:{},max speed:{})'.format(self.brand, self.max_speed))

if __name__ == '__main__':

    audi = Car()
    audi.set_brand('Audi')
    audi.set_max_speed(200)
    audi.print_data()

    benz = Car('Mercedez Benz', 180)
    benz.print_data()

