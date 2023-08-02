# class maschine:
#     def __init__(self, mark, model, power, price):
#         self.mark = mark
#         self.model = model
#         self.power = power
#         self.price = price
#     def _change_power(self,new_power):
#         self.power = new_power
#     def __str__(self):
#         return f'mark: {self.mark} , model: {self.model}, power: {self.power}, price: {self.price}'
# car1 = maschine('toyota', 'camry', '100', '10000')
# print(car1)
# car1._change_power('200')
# print(car1)


# создать класс проект с названием датой начала
# дата дедлайна список имен програмистов задействованых в нем
# (дата начала автоматом при создании обьекта)
# с возможностью измения даты окончания
# ввод програмистов новых и удаление уволенных
# import datetime
# class Project:
#     def __init__(self, name, start_date, finish_date, programers):
#         self.name = name
#         self.start_date = datetime.datetime.now()
#         self.finish_date = finish_date
#         self.programers = programers
#     def add_programer(self, new_programer):
#         self.programers.append(new_programer)
#     def _change_finish_date(self, new_finish_date):
#         self.finish_date = new_finish_date
#     def _remove_programer(self, new_programer):
#         self.programers.remove(new_programer)
#     def __str__(self):
#         programisters = ' '
#         for programers in self.programers:
#             programisters += '\t' + programers + '\n'
#         return f'name: {self.name},\n start_date: {self.start_date}, \n finish_date: {self.finish_date},\n programers: {programisters}'
# project1 = Project('programmator', '2022-01-01', '2022-12-31', ['peter','alexey','ferdinand'])
# print(project1)
# project1.add_programer('ivan')
# print(project1)
# project1._change_finish_date('2024-01-01')
# print(project1)
# project1._remove_programer('peter')
# print(project1)

# Создать класс User, у которого будут:
# Имя
# Фамилия
# Логин (не менее 5 символов)
# Пароль (не меньше 8 символов и должен содержать минимум 3 буквы).
#
# Все поля должны быть скрытыми.
# К каждому атрибуту написать по два метода.
#
# Для вывода пользователя метод str не использовать.

class User:
    def __init__(self, name, surname, login, password):
        self.__name =name
        self.__surname = surname
        self.__login = login
        self.__password = password
    def set_login(self, new_login):
        if len(new_login) >= 5:
            self.__login = new_login
    def set_password(self, new_password):
        # проверка на наличе  минимум 3 букв
        cnt = 0
        new_passwordList = list(new_password)
        for i in new_passwordList:
            if i.isalpha():
                cnt += 1
        if len(new_password) >= 8 and new_password != ' ' and cnt >= 3:
            self.__password = new_password
    def __str__(self):
        return f'name: {self.__name},\n surname: {self.__surname},\n login: {self.__login},\n password: {self.__password}'

user1 = User ('ivan', 'ivanov', 'ivannov', 'vf1234')
print(user1)
user1.set_login('ivan1')
print(user1)
user1.set_password('ivd12346')
print(user1)