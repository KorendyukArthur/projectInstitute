print("Практика,задание 1")
a = 3
b = 7
c = 12
for i in range(1):
    print(a)
    print(b)
    print(c)

print("Практика,задание 2")
a = int(input())
if a <= 10:
    print("меньше 10")
else:
    print("больше 10")


print("Практика задание 3")
b = int(input())
if b <= 10:
    print("первое сообщение")
elif b >= 10 and b <= 25:
    print("Второе сообщение")
elif b >= 25:
    print("Третье сообщение")


print("Практика задание 4")
a = 13
b = 6
c = a % b
print(c)

print("Практика задание 5")

a1 = int(input())
a2 = int(input())
c1 = a1 // a2
print(c1)


print("Практика задание 6")
age = int(input())
if age <= 14:
    print("ребенок")
elif age >= 14 and age <= 21:
    print("Подросток")
elif age >= 21 and age <= 40:
    print("джентельмен")
else:
    print("Пожилой")
