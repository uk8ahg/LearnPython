from random import randint
mes="Ты сделал {} попыток"
print("Я загадаю число от 1 до 100,а ты попробуй отгадать")
#Тут будет рандомайзер
up=0
low=0
while True:
    low=randint(1,101)-randint(1,5)
    up=randint(1,101)+randint(1,5)
    if up>low and low>=1 and up<=101:
        biba=randint(low,up)
        break
#Ответы игрока
count_try=0
print("Твой ход!")
while True:
    count_try+=1
    boba=int(input())
    if boba>biba:
        print("Число должно быть меньше")
    elif boba<biba:
        print("Число должно быть больше")
    elif boba==biba:
        print("ТЫ ВЫИГРАЛ!!!!!")
        break
print(mes.format(count_try))
