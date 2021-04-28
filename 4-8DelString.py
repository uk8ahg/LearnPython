n=input("Введите числа разделенные пробелами\n").split()
ind=int(input("Введите индекс\n"))
for i in range(len(n)):
    n[i] = int(n[i])
print("Список до сдвига",n)
n.pop(ind)
print("Список после сдвига",n)
