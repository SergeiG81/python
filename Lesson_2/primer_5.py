list = [9, 8, 7, 7, 6, 5, 3, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтинга в виде натурального числа: '))
i = 0
for n in list:
    if new_number <= n:
        i += 1
list.insert(i, new_number)
print(list)