print("Задание 1")
s = ["Ходячие мертвецы","Красавиц","Клан сопрано","Дневники вампира"]

for i in s:
    print(i)
sd = 0
print("Задание 2")
for i in range(25,51):
    print(i)

print("задание 3")
for i in s:
    print(i)
    d = s.index(i)
    print(d)

print("Задание 4")
lst = [1,2,3,4]
while True:
    a = input("Введите число или Х для выхода")
    if a == "X" or a == "x":
        break
    if int(a) in lst:
        print("Правильное число")
        break
    else:
        print("Не то число")

print("Задание 5")
list1 = [8,19,148,4]
list2 = [9,1,33,83]
obsh = []
for i in list1:
    for j in list2:
        obsh.append(i * j)
print(obsh)

while True:
    s = input("Введите число")
    if s == "a":
        print("Правильно")
        break
    elif int(s) in lst:
        print("Правильно")
        break
    else:
        print("неправильно")


        


            

    
