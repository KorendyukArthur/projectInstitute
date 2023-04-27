deistvie1 = "сесть"
deistvie2 = "обрадоваться"
if deistvie1 == "встать":
    print ("не правильное действтвие")
else :
    print ("правильное дествие")
    
if deistvie1 == "сесть":
    print("опачки")

print("Действие с условными конструкциями")
x = 17
if x == 17:
    print("число 17")
if x >= 5:
    print("число больше 5")
if x <= 5:
    print("число меньше 5")
if x % 2 == 0:
    print("четоное число")
if x % 2 != 0:
    print( "нечетное число")

if x >= 5 and x <= 12:
    print("условие выполнено")

if x >= 5:
    if x <= 20:
        print("волженный цикл")


print("инструкции с elif")

home1 = "USA"
if home1 == "Япония":
    print("привет Япония")
elif home1 == "Венеция":
    print("привет Венеция")
elif home1 == "Нидерланды":
    print("привет Нидерланды")
elif home1 == "USA":
    print("привет Америка")
else:
    print("Good")
x = 36
if x <= 18:
    print("Несовершеннолетний")
elif x >= 18 and x<= 35 and x == 35:
    print("Человек среднего возраста")
elif x >=35 and x<= 55 and x != 35:
    print("человек несомненно старый")
else:
    print("Динозавр")

print("введите число")
a = int(input())
if a <= 10 or a == 10:
    print("Низкий уровень")
elif a >= 10 and a <= 20:
    print("средний уровень")
else:
    print("высокий уровень")
if a >= 20 and a != 20 and a <= 30:
    print("Высокий уровень номер один")
else:
    for i in range(4):
        print(a)
if a % 2 == 0:
    print("четное число")
if a % 2 != 0:
    print("нечетное число")

    


    




    










