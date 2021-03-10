line = input("Введите слова через пробел: ")
a = line.split()
for i in range(len(a)):
    if len(a[i]) <= 10:
        print('string', i + 1, '-', a[i])
    else:
        print('string', i + 1, '-', a[i][:10])



