'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

import math

class A:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = math.fabs(x1)
        self.y1 = math.fabs(y1)
        self.x2 = math.fabs(x2)
        self.y2 = math.fabs(y2)
        self.x3 = math.fabs(x3)
        self.y3 = math.fabs(y3)
        self.ab = round(math.sqrt(math.pow((self.x2-self.x1), 2)+math.pow((self.y2-self.y1), 2)))
        self.bc = round(math.sqrt(math.pow((self.x3-self.x2), 2)+math.pow((self.y3-self.y2), 2)))
        self.ca = round(math.sqrt(math.pow((self.x3-self.x1), 2)+math.pow((self.y3-self.y1), 2)))
        self.p = self.per / 2

    @property
    def per(self):
        return self.ab + self.bc + self.ca

    @property
    def square(self):
        return round((self.ca/2)*self.heght_ca)


    @property
    def heght_ca (self):

        return round(2*(math.sqrt(self.p*(self.p-self.ab)*(self.p-self.bc)*(self.p-self.ca)))/self.ca)


treugolnik = A(0, 0, 5, 12, 10, 0)

print('Площадь: {}'.format(treugolnik.square))
print('Высота: {}'.format(treugolnik.heght_ca))
print('Периметр: {}'.format(treugolnik.per))