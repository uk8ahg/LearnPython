s=input("Введите строку символов с пробелами\n")
s1=""
for i in s:
    if i !=" ":
        if i not in s1:
            s1+=i
print(s1)
