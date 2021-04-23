#Вводится строка слов, разделенных пробелами. Найти самое длинное слово и вывести
#его на экран. Случай, когда самых длинных слов может быть несколько, не
#обрабатывать.

print("Введите строку, в которой слова разделены пробелами")
list=input()
list=list.split(" ")
cot=0
result=""
result1=""
for word in list:
      result=word
      if cot<len(result):
            cot=len(result)
            result1=result
print("Самое длинное слово:",result1)
