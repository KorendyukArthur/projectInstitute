print("задание 1")
for i in range(0,11):
    print(i)

print("задание 2")
rest = False
while rest == False:
    try:
        q1 = int(input("Введите число"))
        for i in range(0,q1):
            print(i)
        rest = True
    except (ZeroDivisionError,ValueError):
        print("неправильно введенные данные")
print("задание 3")
