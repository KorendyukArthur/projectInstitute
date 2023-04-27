print("начальный пример")
def f(x):
    return x * 12
result = f(2)
print(result)

def d(e):
    return e + 1
result1 = d(3)
print(result1)
result1 = d(5)
print(result1)


def newModul(d, e ,f):
    return d * 2 + e * 2 + f * 2
result = newModul( 3, 3 ,4)
print(result)


res = d(2)
print(res)


def f(x):
    return x+1
z = f(int(input()))

if z == 5:
    print ("всего 5")
else:
    print ("нет")

    #фуекция
    #посчитать налог с трех магазинов
def namemod(x,y,z) :
    return (x+y+z)/100 * 30


s = namemod(int(input()),int(input()),int(input()))
print(s)

if s <= 30:
    print("до 30 процентов")
elif s >= 30 and s <= 40:
    print("от 30 до 40 процентов")
elif s >=40 and s<=50:
    print("от 40 до 50")
else:
    print("не выгодно")

print("введите третью переменную для расчета")
name1 = namemod(3, 15, int(input()))
print("производится вычисление")
if name1 <= 100:
    print(name1)
else:
    print("больше 100")


def d():
    return 1+3
result = d()
print(result)













