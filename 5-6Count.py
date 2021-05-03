def counter(num):
    count_d=0
    count_e=0
    count_d=num//10
    count_e=num-(count_d*10)
    return (count_d, count_e)

n=int(input('Введите двузначное число\n'))
print(counter(n))
