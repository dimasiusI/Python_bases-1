# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re
import sys

def add(dir_):
    i = 1
    while i <= 9:
        try:
            os.mkdir(os.path.join(os.getcwd(), dir_+str(i)))
        except FileExistsError:
            print('Такая директория уже существует')

        i += 1

add('dir_')

def rem(dir_):
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_))
    except FileExistsError:
        print('Такая директория не существует')
    except FileNotFoundError:
        return

len_ = len(os.listdir(os.getcwd()))

i = 1
while i <= len_:
    rem('dir_'+str(i))
    i += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

def is_dir(dir_):
    if os.path.isdir(dir_):
        print(os.path.basename(dir_))

for f in os.listdir(os.getcwd()):
    is_dir(f)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

copy_dir = os.path.abspath('for_copy')
if not os.path.exists(copy_dir):
    os.makedirs(copy_dir)

os.system('copy %s %s' % (sys.argv[0], copy_dir))
