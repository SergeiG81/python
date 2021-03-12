'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших
двух аргументов.
'''

def my_func(*params):
    result2 = 0
    for n in params:
        result2 += n
    result1 = min(*params)
    result = result2-result1
    return result
print(my_func(-5,-3,-8))