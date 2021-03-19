'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

'''
with open('file_3.txt', 'r', encoding="utf-8") as my_file:
    salary = []
    persona = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           persona.append(i[0])
           salary.append(i[1])
print(f'Оклад меньше 20.000 {persona}, средний оклад {sum(map(float, salary)) / len(salary)}')
