print("Цикл for, функция range")
print("первый пример")
for i in range(1,11):
    print(i)

spisok = [1,2,3,4,5,6,7]
d = 0
for i in spisok:
    d += i
d1 = d/3
print(d1)

for i in range(1,11):
    print("Море")


print("Использование цикла while")

x = 10
while x > 0:
    print(x)
    x -=1
print("Вот так")

x = 3
s = ["s","d","e","k"]
while x >= 0:
    print(s)
    x -= 1

x = 5
while x >= 0:
    for i in s:
        print(i)
    x -= 1
    
print("Программма использующая цикл и break")

spisk = ["Один","Два","Три","Четыре"]
n = 0

while True:
    print("Введите букву X для выхода")
    a = input(spisk[n])
    if a == "X":
        break
    n = (n+1)%4

while True:
    print("Введите Х для выхода")
    a1 = input(spisk[n])
    if a == "X":
        break
    n = (n +1) % 4
    if n == 2:
        continue
   
    


















