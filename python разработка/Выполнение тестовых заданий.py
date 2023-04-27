print("s1")
print("s2")
print("s3")

def func(x):
    if x < 10:
        print("меньше")
    else:
        print("больше")
func(8)

def func1(x):
    if x <=10:
        print("1")
    elif x >=10 and x <= 25:
        print("2")
    else:
        print("3")

func1(15)

def func2(x,y):
    result = x % y
    print(result)

func2(14,11)

def func3(x,y):
    result1 = x // y
    print(result1)
    
func3(16,3)

def func4(age):
    if age == 12:
        print("on")
    else:
        print("non")

func4(12)

def func5():
    #x = int(input())
    x = 3
    result = x ** 2
    print(result)
func5()

def func6():
    #st = input("Введите строку: ")
    st = "aaaabbbbcccc"
    print(st)

func6()

def func7 (x,y,z,c1=12,c2=24):
    return x + y + z + c1 + c2

print(func7(1,2,3))


def func8 (x):
    return x / 2
def func9(y):
    result1 = y * 4
    print(result1)


a1 = func8(5)
func9(a1)

def func10():
    try:
        st = "34"
        st = float(st)
        print(st)
    except(ValueError):
        print("Неверный тип данных")

func10()

print("Глава 5")

list1 = ["первый музыкант ","Второй музыкант","Третий музыкант"]
print(list1)

kort = ("13","24")
kort1 = ("14","15")


s = "13" in kort
print(s)

slov = {"1":"рост","2":"вес","3":"цвет"}
print(slov)

def func11():
    #x = input("Введите ваш рост")
    #y = input("Введите ваш цвет")
    #z = input("Введите ваш вес")

    x = 1
    y = 3
    z = 3
    if x in slov:
        s = slov[x]
        print(s)
    else:
        print("Не тот рост")
    if y in slov:
        s1 = slov[y]
        print(s1)
    else:
        print("Не тот цвет")
    if z in slov:
        z1 = slov[z]
        print(z1)
    else:
        print("Не тот вес")

func11()

def func12():
    slov1 = {"Адамс":("mic1","mic2"),"revis":("mic5","mic6")}
    s = slov1["Адамс"]
    print(s)

func12()
    
print("str")

a = "Чехов"
for i in a:
    print(i)

a = "стихотворение"
b = "фелармонию"
c = "вчера я написал {}. Вчера я ходил {}".format(a,b)
print(c)

d = "олдос родился в 1983 году."
d1 = d.upper()
print(d)

e = "Где это? Кто это? Как это?"
e1 = e.split("?")
print(e1)

f = ["Рыжая","лиса","перепрыгнула"]
result = " ".join(f)
print(result)

f1 = ["Где", "это", "было", "видано"]
result1 = " ".join(f1)
print(result1)

g = "Хеменгуэй"
g1 = g.index("э")
print(g1)

h = "Ребенок зеркало родителей"
h1 = h.replace("о","0")
print(h1)

i = "три"
i1 = i * 3
print(i1)

j = "Первый опыт! Вторая программа"
j1 = j[0:11]
print(j1)

print("Циклы")

list1 = ["один","два","три"]
for i in list1:
    print(i)

for i in range(25,51):
    print(i)

for i in list1:
    print(i)
    print(list1.index(i))
    
x = 0
while input("введите Д для окончания или П для продолжения:") != "Д":
        print("один")


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
mass = []
for i in list1:
    for j in list2:
        mass.append(i+j)

print(mass)
        











        
