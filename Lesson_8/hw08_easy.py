'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''

class Bilder:
    def __init__(self, a, b):
        self.dict = dict(zip(a, b))
        for key, value in self.dict.items():
            setattr(self, key, value)

workers = ['Petr', 'Ivan', 'Sonya', 'Vasya']
hours = [10, 20, 30, 40]

do = Bilder(workers, hours)

print(do.Ivan)



'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''

class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
x.clear()
print(x.wrapped)