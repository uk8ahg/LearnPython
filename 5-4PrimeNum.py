def prime(n):
    div = 2
    while n % div != 0 :
        div += 1
    if div == n:
        return True
    else:
        return False

num=int(input("Введите число от 1 до 1000\n"))
print(prime(num))
