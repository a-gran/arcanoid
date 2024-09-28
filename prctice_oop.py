#class User
#свойства: имя, возраст, пол, email (name, age, gender, email)
#методы: печать информации о себе (print_info())
#Задание: создать объект user1 и вывести информацию о нем

class User:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def print_info(self):
        print(f' Имя: {self.name}\n Возраст: {self.age}\n Пол: {self.gender}\n Email: {self.email}')

user1 = User('Иван', 25, 'мужской', 'ivan@mail.ru')
user1.print_info()
