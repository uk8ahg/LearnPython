number=[]
while True:
      num=int(input("Введите число\n"))
      if num==0:
            break
      else:
            number.append(num)
print("Сумма всех чисел:",sum(number))
