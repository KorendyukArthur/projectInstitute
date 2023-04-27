def f(x=2):
    
    return x**x
print(f())
print(f(5))


def nameA(z, x , y = 10) :
    print("Введите z")
    z = int(input())
    return x + y + z

result = nameA(10,5)
print(result)



result1 = nameA(10,3)
print(result1)



x = 100
def f1():
    global x
    x+= 1
    print(x)

f1()

r1 = 1
r2 = 2
r3 = 3
def f2():
    s = r1
    s += 10
    print(s)
    print(r2)
    print(r3)


f2()

# обработка исключений
print("введите число: ")
x = int(input())
try:
    if x <= 18:
        print(18/x)
        print("десять")
    elif x >=18 and x <= 30:
        print("больше десяти")
except ZeroDivisionError:
    print("что то не так")



    






    
