print("небольшая встроенная функция")
a = len("sa")
print(a)
print("введите слово для расчета символов")
text = len(str(input()))
print(text)




def nameS(s):
    len(s)

print("Введите слово для расчета")
s = len(str(input()))
if s <= 5:
    print("короткое слово")
    if s % 2 == 0:
        print("четное")
    elif s % 2 != 0:
        print("не четное")
elif s >=5 and s <= 10:
    print("среднее слово")
    if s%2 == 0:
        print("Четное")
    elif s%2 != 0:
        print("не четное")
else:
    print("длинное слово")
    if s%2 == 0:
        print("четное")
    elif s%2 != 0:
        print("не четное")
print(s)

d = len("good")
print(d)

print("функция стринг")
r = str(100)
print(r)

print("функция инт")
r1 = int(122)
print(r1)


print("функция флоат")
r2 = float(123)
print(r2)

def named1(inst):
    return inst + 15
z = named1(int(input()))
print(z)


age = input()
new_age = int(age)
if new_age >= 16:
    print("Получить паспорт")
else:
    s = named1(new_age)
    print(s)






          \

