#Найти в строке указанную подстроку и заменить ее на новую. Строку, ее подстроку для
#замены и новую подстроку вводит пользователь.

s=input("Введите строку\n")
source=input("Введите строку которую хотите заменить\n")
target=input("Введите на что будем менять\n")
s=s.replace(source,target)
print(s)
