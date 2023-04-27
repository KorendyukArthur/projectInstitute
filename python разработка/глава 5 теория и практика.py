'''контейнеры это как кортатеки, в питон используются часто: списки, кортежи, словари.'''
''' сначало объявляется переменная, далее пишется словои через точку имя метода'''

'''Программа номер один, работа методов'''
a = "Привет".replace("т","r")
print(a)
b = input("Введите слово :")
print(b)

c = b.replace("d", "С")
print(c)

'''Списки'''
'''создане пустого списка'''
newspisc = list()
print(newspisc)
'''так же создание пустого списка []'''
newspisc1 = []
print(newspisc1)
'''создание списка с элементами внутри'''

newspisc2 = ["первый","второй","третий"]
print(newspisc2)
'''добавление нового лемента'''
newspisc2.append("четвертый")
print(newspisc2)


'''создание нового списка с функцией и циклом'''
newspisc3 = ["минимум","серний","максимум"]
x = int(input())
def shtorm(x, y =2):
    s = x * y
    print(s)
if x >= 0 and x <= 10:
    s1 = shtorm(x)
else:
    newspisc3.append("перебор")
    print(newspisc3)

'''созздание нового списка и хранение любых типов данных'''
name = []
name.append(False)
name.append(99)
name.append("список")
name.append(3.4)
print(name)

