'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''


class First:
    def __init__ (self, a, b):
        self.class_2 = Second(a, b)

    def __getattr__(self, attr):
        return getattr(self.class_2, attr)

class Second:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    @property
    def del_1(self):
        return self.a % self.b

    @property
    def del_2(self):
        return self.a / self.b

    @property
    def del_3(self):
        return self.a // self.b

x = First(10, 2)

print(x.del_1)
print(x.del_2)
print(x.del_3)

