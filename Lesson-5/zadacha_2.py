'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.

'''
f1 = open('file_2.txt', 'r', encoding="utf-8")
content = f1.readline()
n_str = 0
n_word = 0
while content != '':
    n_str = n_str + 1
    string = content.split()
    n_word = len(string)
    print("в строке", n_str, "-", n_word, "слов")
    content = f1.readline()
f1.close()
print("количество строк =", n_str)
