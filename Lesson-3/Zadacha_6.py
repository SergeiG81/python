'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(s):
    return s.capitalize()

string = input("Введите слово из латинских букв в нижнем регистре: ")
print(int_func(string))

def int_func(s):
    return s.capitalize()

my_list = input(
    "Введите слова из латинских букв в нижнем регистре через пробел: ").split()

for i in range(len(my_list)):
    print(int_func(my_list[i]), end=' ')