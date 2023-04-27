import math #Операции с функцией
import random #Функция для случайных чисел
import statistics #модуль подсчета среднего значения
import keyword #модуль поиска значений
import sys
sys.path.insert("","C:/Users/Артур/Desktop/tstp/hello")
import hello

print("з1")
p = math.pow(2,2)
print(p)

print("з2")
p2 = random.randint(0,100)
print(p2)

print("з3")
p3 = random.randint(0,100)
print(p3)

print("з3")
p4 = random.randint(1,10)
if p4 >= 5:
    print(random.randint(1,1000))
else:
    print(random.randint(1,100)*(-1))

random.randint(1,2)

print("з4")
#функция среднее : mean
#функция медиана : median
#функция мода : moda
s1 = [1,2,3,4,5,6,7,8]
p5 = statistics.mean(s1)
print(p5)
p6 = statistics.median(s1)
print(p6)
p7 = statistics.mode(s1)
print(p7)



print("з5")
#функция keyword
p8=keyword.iskeyword("if")
p9=keyword.iskeyword("for")
p10=keyword.iskeyword("go")
print(p8)
print(p9)
print(p10)



s = statistics.mode(s1)
print(s)


s34 = hello.print_hello()




