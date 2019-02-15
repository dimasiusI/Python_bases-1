'''
Задание_1. Создайте свое исключение для проверки вводимого числа.
Исключение должно возбуждаться, если пользователь ввел отрицательное число.
Также предусмотрите тот, случай, что пользователь ввел не число, а строку
(здесь можно применить встроенное исключение).
'''

class InputError(Exception):

    def __init__(self, n):
        Exception.__init__(self)
        self.n = n

    def __str__(self):
        return 'InputException: Число {} меньше 0; ' \
               'ожидалось, как минимум, 1'.format(self.n)

def max_chars(n):
    if n < 0:
        raise InputError(n)


try:
    n = int(input('Введите число: '))
    max_chars(n)
except InputError as ex:
    print(ex)
except TypeError:
    print('Вы ничего не ввели или ввели не число.')
except ValueError:
    print('Вы ничего не ввели или ввели не число.')
else:
    print('Не было исключений.')
finally:
    print('Успех!')