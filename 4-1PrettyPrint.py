dict={'name':['Amin','Roman','Iroda'],
      'age':[16,19,27],
      'sex':['m','m','f']}
count=0
while count<(len(dict.get('name'))):
      for e in dict:
            x=dict.get(e)
            a=x[count]
            print(a)
      count+=1
      print("-------------------------------")
