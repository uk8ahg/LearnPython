#Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
#Например, если было введено "abc cde def", то должно быть выведено "abcdef".

s=input("Введите строку символов с пробелами\n")
s1=""
for i in s:
    if i !=" ":
        if i not in s1:
            s1+=i
print(s1)
