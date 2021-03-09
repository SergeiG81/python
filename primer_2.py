list = input('Введите элементы списка: ').split()

if len(list) %2 == 0: # проверка на четность
    for i in range(0,len(list)-1,2):
        list[i],list[i+1] = list[i+1],list[i] # обмен значений
        
else:
    for i in range(0,len(list)-2,2):
        list[i],list[i+1] = list[i+1],list[i]
        
print(list)

