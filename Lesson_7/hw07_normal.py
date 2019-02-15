'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix:
    def __init__ (self, list1):
        self.list1 = list1
        self.mis = self.get_str()

    def get_str (self):
        r = ''
        for i in self.list1:
            r += str(i).replace(',', ' ').replace('[', '|').replace(']', '|') + '\n'
        return r

    def __add__ (self, other):
        res = []
        for i in range(len(self.list1)):
            row = []
            for j in range(len(self.list1[0])):
                row.append(self.list1[i][j] + other.list1[i][j])
            res.append(row)
        return Matrix(res)

    def __str__ (self):
        return self.mis


matrix1 = Matrix([[1,2,3,5], [1,2,3,6], [1,2,3,7]])
matrix2 = Matrix([[1,2,3,5], [1,2,3,6], [1,2,3,7]])

print('Результат сложения матриц: ')
print(matrix1+matrix2)