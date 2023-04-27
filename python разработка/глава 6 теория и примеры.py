lisq = []
lisq.append("a1")
lisq.append("a2")
li = lisq[1]
print(li)

try:
    author = "Genry"
    a1 = author[4]
    print(a1)
except(IndexError):
    print("Введенный индекс находется вне предела")

newstring = "одиннадцать"
a2 = newstring[-2]
print(a2)

newstring1 = "два"
a3 = newstring1[-2]
print(a3)
if str(a3) == "в":
    print("работает правильно")
else:
    print("ощибка")


print("сложение строк")
s1 = "первый"
s2 = "второй"
s3 = "третий"
o1 = s1 + s2 + s3
print(o1)

print("умножение строки")
s4 = "три строки на трех строках"
o2 = s4 * 3
print(o2)

print("изменение реггистра")
s5 = "перва строчка изменение регистра"
o5 = s5.upper()
print(o5)

s6 = "НОВЫЙ ДЕНЬ"
o4 = s6.lower()
print(o4)

s7 = "опять что то"
o3 = s7.capitalize()
print(o3)

print("метод изменения строки и делающий окна для ввода")
s8 = "{} где то {} машина"
name1 = "когда то"
name2 = "ехала"
o6 = s8.format(name1,name2)
print(o6)


s9 = "{} был {}"
o7 = s9.format("это", "январь")
print(o7)

new1 = str(input())
new2 = str(input())
new3 = str(input())
s10 = "Это был {}, {}, {}".format(new1,new2,new3)
print(s10)



i1 = int(input("Введите логин:"))
i2 = int(input("Введите пароль:"))
gol1 = "Вы ввели логин: {} и пароль{}".format(i1,i2)
def s1(i1,i2):
    return gol1


if i1 > i2:
    s = s1(i1,i2)
    print(s)
else:
    print("i2 > i1")


print("метод split - разделение строки")

i = input("Введите два предложения:")
de = input("Введите число:")
slov = {}
slov[1] = "1"
slov[2] = "2"
slov[3] = "3"
slov[4] = "4"
print(slov)

spisok = []
spisok.append("22")
e1 = print(spisok)
def newr():
    return e1

if de in slov:
    slov[5] = "5"
    print(slov)
else:
    newr()
    r = i.split(".")
    print(r)
    




























