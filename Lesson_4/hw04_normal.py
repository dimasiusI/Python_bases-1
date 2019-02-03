# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

str = "mtMmEZUOmcq"

pattern = '[a-z]+'

lst = re.findall(pattern, str)

print(lst)

lst = ""

for i in str:
  if i == i.lower():
    lst += i
  else:
    i = ' '
    lst += i

lst = lst.split(' ')
lst = [i for i in lst if i != '']

print(lst)


# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

lst_g = [random.randint(0, 9) for _ in range(2500)]

r = "".join(str(x) for x in lst_g)

print(r)

f = open('2500.txt', 'w')

f.write(r)

f.close()

f = open('2500.txt', 'r')

r = []

for i in f:
     r.append(i)

r = [int(j) for j in r]

print(r)

num = ""
num_max = ""
count_ = 1
count_max = 0

for el in range(len(r) - 1):
    if r[el] == r[el + 1]:
        num = r[el]
        count_ += 1
        if count_max < count_:
            count_max = count_
            num_max = num
    else:
        if count_max < count_:
            count_max = count_
            num_max = num
            count_ = 1
            num = ""
        else:
            count_ = 1

print("Сколько раз повторилась: {}, Какая цифра: {}".format(count_max, num_max))






