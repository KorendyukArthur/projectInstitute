name = "Поле"
for family in name:
    print(family)

print("Перебор списка циклом")

name2 = ["грустные души","Опять пять","Где мир"]
for de1 in name2:
    print(de1)

print("перебор кортежа циклом")

name3 = ("первый всплеск","Новая заря","Сильный ветер")
for de2 in name3:
    print(de2)

print("перебор ключей в словаре")
name4 = {"1":"один","2":"два","3":"три","4":"четрые"}
for de3 in name4:
    print(de3)

print("изменение элементов")
name5 = ["Первый день","Второй день","Третий день"]
i = 0
for de4 in name5:
    new = name5[i]
    new = new.upper()#изменение регистра"""
    name5[i] = new
    i += 1
print(name5)

print("Изменение элементов")

namee1 = ["Солные ","Свет","Имение"]
i = 0
for de5 in namee1:
    new1 = namee1[i]
    new1 = new1.upper()
    namee1[i] = new1
    i += 1
print(namee1)


spisk = ["Голодный","Сумрочный","Искушение"]
i = 0
for newper in spisk:
    newper2 = spisk[i]
    newper2 = newper2 + "новое"
    spisk[i] = newper2
    i += 1
    print(spisk)


for i, show in enumerate(spisk):
    new = spisk[i]
    new = new.upper()
    spisk[i] = new
print(spisk)


newsp = ["Первый","Второй","Третий"]
newsp1 = ["Четвертый","Пятый","Шестой"]
all_newsp = []

for met in newsp:
    met = met.upper()
    all_newsp.append(met)

for met2 in newsp1:
    met2 = met2.upper()
    all_newsp.append(met2)
print(all_newsp)



#в с 13 15 16

#наме 13
#наме 15
#наме 16
s = 0
s1 = []
r = [222,234,233]
d = 0

re = []
for ise in r:
    s = r[d] #222
    s1.append(s)
    d += 1
print(s1)

schetchik = 0
suma = 0
numbers = [3,4,5,6]

for i in numbers:
    suma += i
    
    schetchik +=1
srednee = suma / schetchik
print("Выведите сумму чисел:",suma)
print("Выведите среднее:",srednee)
      


numbers = [3, 4, 5, 6]
count = 0
schetchik = 0

for i in numbers:
    count += i
print(count)

numbers = []
s = []
d = 0
kolvo_chisel = int(input())
chisla = input().split()
for der in chisla:
    s.append(der)
    
for i in range(kolvo_chisel + 1):
    d += i
print(d)





a2 = []
a3 = []
d = 0
a1 = int(input("Введите колличество чисел:"))
a2 = input("Введите числа через пробел").split()


for i1 in a2:
    a3.append(i1)
for i in range(a1 + 1):
    d += i
print(d)

lst = [5,6,4,3]

def more_than_five(lst):
    for i in lst:
        r1 =  i and i >= 5
        d1 = r1
        if r1 == True:
            print(d1)

more_than_five(lst)



tv = ["Первый","Второй"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)




































