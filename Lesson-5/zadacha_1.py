my_file = open('file_1.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
my_file.close()

my_file = open('file_1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()