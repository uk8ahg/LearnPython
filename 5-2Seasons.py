def month(m):
    dict_m={'winter':[1,2,12],
            'autumn':[9,10,11],
            'spring':[3,4,5],
            'summer':[6,7,8]}
    for e in dict_m.keys():
        if m in dict_m.get(e):
            return (e)

mont=int(input("Ведите номер месяца\n"))
print(month(mont))
