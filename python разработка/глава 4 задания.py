print("задание первое")
'''вводится первая функция возведения в степень, вся работа в функции'''
def name1(x = 1):
    print("Введите x")
    x = int(input())
    s = int(x ** 2)
    print (s)
name1()



'''вторая функция возведения в степень, часть работы отделено от функции'''
def name2(x):
    return x ** 2
print("Введите переменную")
r = int(input())
d = name2(r)
print(d)


print("задание второе")
'''по заданию функция принимает строку и возвращает ее'''
def name3(x):
    return x
print("Введите слово")
x = (input())
d = name3(x)
print(d)


print("задание третье")
'''функция #1 принимающая три обязательных параметра и два необязательных'''
def name4(x,y,z,n1=12,n2=15):
    return x+y+z+n1+n2

s = name4(1,2,3)
print(s)

'''функция №2 принимающая три обзательных параметра и два необязательных'''

def name5(x1,x2,x3,x4 = 12,x5 =13):
    if x1 >= 10:
        return x1+x2+x3+x4+x5
    else:
        return (x1+x2+x3+x4+x5) ** 2

s = name5(3,4,5)
print(s)

s1 = name5(11,4,5)
print(s1)

print("задание четвертое")
''' первая функция принимаеет целое число и возвращает результат деления
после чего отправвлет результат во второую функцию'''

a = int(input())
def new4func(a):
    return a / 2
result = new4func(a)
print(result)
result = int(result)
print(result)

def newfunc(result):
    return result * 4
result2 = newfunc(result)
print(int(result2))


print("задание пятое")


a1 = input("Ввод строки для птяого задания:")
try:
    def newfunc3 (a1):
        return float(a1)
    rez1 = newfunc3(a1)
    print(rez1)
except(ValueError):
    print("Неправильно значение")
    
print("задание шестое")
'''было выполнено и коментарии необльшие были написаны'''




















