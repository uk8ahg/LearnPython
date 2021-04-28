print("Этот калькулятор позволяет Вам проводить основные")
print("арифметические операции (+,-,*,/)")
print("Для окончания работы программы введите 0")
print("")
operation = ""
arg1 = 0
arg2 = 0
mes=["Введите 1-е слагаемое\n","Введите 2-е слагаемое\n","Введите уменьшаемое\n","Введите вычитаемое\n","Введите 1-й множитель\n","Введите 2-й множитель\n","Введите делимое\n","Введите делитель\n"]
while True:
      while True:
            op = input("Введите символ операции или 0 для выхода\n")
            if op != "+" and op != "-" and op != "*" and op != "/" and op != "0":
                  print("Пожалуйста, посторите ввод знака оперции (+,-,*,/) или 0 для выхода")
            else:
                  operation = op
                  break
      if operation=="0":
            break
      while True:
            if operation=="+":
                  x1 = input(mes[0])
            elif operation=="-":
                  x1 = input(mes[2])
            elif operation=="*":
                  x1 = input(mes[4])
            elif operation=="/":
                  x1 = input(mes[6])
            if x1.isdigit():
                  arg1=int(x1)
                  break
            else:
                  print("Это не число!! Повторите ввод!")
      while True :
            if operation == "+" :
                  x2 = input(mes[1])
            elif operation == "-" :
                  x2 = input(mes[3])
            elif operation == "*" :
                  x2 = input(mes[5])
            elif operation == "/" :
                  x2 = input(mes[7])
            if x2.isdigit():
                  if x2 !='0':
                        arg2 = int(x2)
                        break
                  else:
                        print("На 0 делить нельзя!!!")
            else :
                  print("Это не число!! Повторите ввод!")
      if operation == "+":
            print("Результат сложения равен",arg1+arg2)
      elif operation == "-":
            print("Результат вычитания равен",arg1-arg2)
      elif operation == "*":
            print("Результат умножения равен",arg1*arg2)
      elif operation == "/":
            print("Результат деления равен",round(arg1/arg2,2))
