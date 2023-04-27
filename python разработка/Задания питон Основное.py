print('задание 1')
print('первая строка')
print('вторая строка')
print('третья строка')

def func1 (x):
    if x >= 10:
        print('1')
    else:
        print('2')
func1(11)

def func2 (x):
    if x <= 10:
        print(1)
    elif x >= 10 and x <= 25:
        print(2)
    else:
        print(3)

func2(24)

def fucn3(x,y):
    result =  x%y
    print(result)

fucn3(6,5)

def func4(x,y):
    res = x//y
    print(res)

func4(7,3)

def func5(arg):
    if arg == '1':
        print(1)
    if arg == "2":
        print(2)

func5("2")

print('раздел 2')

def func6():
    x = 3
    #вместо 3 вводится int(input('Введите число:')
    x = int(x)
    try:
        res = x * x
        print(res)
        return res
    except:
        print('ошибка')
func6()

def func7():
    x = 3
    #x = input("Введите строку")
    if (isinstance(x,str)):
        print(x)
    else:
        print("error")

func7()


