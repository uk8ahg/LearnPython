def summa(s,y):
    c=0.0
    c=s/10
    for i in range(y):
        c = s / 10
        s=s+c
    return round(s,2)

sum=0
year=0
sum=int(input("Введите сумму вклада\n"))
year=int(input("Введите колличество лет\n"))
print("Итого",summa(sum,year))
