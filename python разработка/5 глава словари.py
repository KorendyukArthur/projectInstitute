'''создание словаря'''

name_dict = dict()
print(name_dict)

name_dict1 = {}
print(name_dict1)

'''создание словаря с вложенными данными ключ - значение'''

name_dict2 = {"ключ1":"значение1","ключ2":"значение2"}
print(name_dict2)

'''добавление в словарь пары ключ - значение'''
name_dict4 = {}
name_dict4["ключ_1"] = "этот ключ нужен для сейфа"
print(name_dict4)

name_dict4["ключ_2"] = "этот ключ нужен для машины"
name_dict4["ключ_3"] = "ключ для холодильника"
name_dict4["ключ_4"] = "ключ для мотоцикла"
name_dict4["ключ_5"] = 1992
print(name_dict4)

'''создание кортежа'''
newcort = ("объем",)
print(newcort)

name_dict4[newcort] = "первый созданный кортеж"
print(name_dict4)


'''определение ключа в словаре'''
s = "ключ_2" in name_dict4
print(s)

s1 = "ключ_17" in name_dict4
print(s1)
del name_dict4["ключ_2"]
print(name_dict4)




new_dict_one = {"1":"доска дуб","2":"доска ясень","3":"доска береза","4":"доска ель"}

chec1 = input()
if chec1 in new_dict_one:
    c1 = new_dict_one[chec1]
    print(c1)
else:
    print("no error")

''' хранение контейнеров друг в друге'''

list_1 = []
list_2 = ["один","два","три","четыре"]
list_3 = ["февраль","январь","декабрь","ноябрь"]
list_1.append(list_2)
list_1.append(list_3)

print(list_1)

a1 = list_1[1]
print(a1)

list_2.append("пять")
print(list_1)
print(list_2)
















