'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
'''


def display_info(name, surname, age, location, email, telefon_number):
    print("Name:", name, "Surname:", surname, "Age:", age, "City:", location, "E-mail:", email, "Telefon:", telefon_number)

display_info(age=22, name="Tom", location="Boston", surname="Wilson", email="aaadk", telefon_number=123532)