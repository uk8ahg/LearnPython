def vis(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False

year=int(input("Введите год\n"))
if vis(year)==True:
    print('Год високосный')
else:
    print('Год не високосный')
