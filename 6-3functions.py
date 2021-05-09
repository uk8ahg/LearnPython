from constant import *

def add_user():
    lst_name=data_dict.get('name')
    n=input('Введите имя\n')
    lst_name.append(n)
    data_dict.update(name=lst_name)
    lst_age=data_dict.get('age')
    a=int(input('Введиет возраст\n'))
    lst_age.append(a)
    data_dict.update(age=lst_age)
    lst_sex=data_dict.get('sex')
    s=input('Введите пол\n')
    lst_sex.append(s)
    data_dict.update(sex=lst_sex)
    print(data_dict)

def del_user():
    n=input('Введите имя\n')
    lst_name = data_dict.get('name')
    lst_age = data_dict.get('age')
    lst_sex = data_dict.get('sex')
    if n in lst_name:
        ind=lst_name.index(n)
        lst_name.pop(ind)
        lst_sex.pop(ind)
        lst_age.pop(ind)
        data_dict.update(name = lst_name)
        data_dict.update(sex = lst_sex)
        data_dict.update(age = lst_age)
        print(data_dict)

def look_user_name():
    n = input('Введите имя\n')
    lst_name = data_dict.get('name')
    lst_age = data_dict.get('age')
    lst_sex = data_dict.get('sex')
    if n in lst_name :
        ind = lst_name.index(n)
        print(lst_name[ind])
        print(lst_age[ind])
        print(lst_sex[ind])
    print(data_dict)
