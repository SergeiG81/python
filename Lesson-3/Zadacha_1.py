''' Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def calc(a, b):
    if b != 0:
        result = ("a / b равно", a / b)
    else:
        result = "Деление на 0!"
    return(result)

print(calc(int(input('a=', )), int(input('b=', ))))

# Еще вариант
def my_func(c, d):
    try:
        result = c / d
        return result
    except ZeroDivisionError as err:
        return "Делитель равен нулю"

my_func(3,0)