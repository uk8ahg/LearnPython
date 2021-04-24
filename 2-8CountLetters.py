#Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной
#строке. Учитывать только английские буквы.

s = input("Введите строку символов с большими и маленькими буквами\n")
BIG="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
message="В строке содержиться {} заглавных букв и {} маленьких букв"
count_big=0
count_small=0

for i in s:
    if i in BIG:
        count_big+=1
    elif i in small:
        count_small+=1
print(message.format(count_big,count_small))
