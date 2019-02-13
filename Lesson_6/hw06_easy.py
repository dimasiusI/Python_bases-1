'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''

class Worker:
    def __init__ (self, name, surname, age, zp, zp_plus):
        self.name = name
        self.surname = surname
        self.age = str(age)
        self.zp = zp
        self.zp_plus = zp_plus
        self._income = {
            'zp' : str(zp),
            'zp_plus' : str(zp_plus)}


worker1 = Worker("Ivan", "Ivanov", 25, 29000, 1000)

print(type(worker1.__dict__))


'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
class Position(Worker):
    def __init__ (self, name, surname, age, zp, zp_plus, percent):
        Worker.__init__(self, name, surname, age, zp, zp_plus)
        self.percent = percent


    @property
    def perc(self):
        oklad_plus_perc = self.zp + (self.zp * (self.percent/100))
        return oklad_plus_perc

    @property
    def full_oklad(self):
        return self.perc + self.zp_plus


    @property
    def get_full_name(self):
        return self.name + ' ' + self.surname + ', ' + self.age + ' years is old'

worker2 = Position("Ivan", "Ivanov", 25, 30000, 6000, 10)

print(worker2.perc)

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах
1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

print(worker2.get_full_name)
print(worker2.full_oklad)




