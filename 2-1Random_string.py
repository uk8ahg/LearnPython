#Вводится строка, состоящая из букв и пробелов. Составить из входящих в нее букв
#несколько любых их сочетаний (слов) любой длины. Каждую букву строки можно
#использовать неограниченное количество раз.

from random import randint
s=input("Введите строку состоящую из строк и пробелов\n")
count_word=randint(2,6)
for i in range(count_word):
    count_letter1=randint(1,50)
    count_letter2 = randint(1, 100)
    if count_letter2>count_letter1:
        res=s[count_letter1:count_letter2]
        print(res)
