print("Цикл 1. Переменные класса и переменные экземпляра")
class Square:
    pass
print(Square)

# у класса есть два типа переменных переменные класса и переменные объектов класса
# переменные объекта класса - синтаксис self.имя_переменной = значение переменной

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {} """.format(self.width,self.len))

n1 = Rectangle(10,100)
n1.print_size()

#переменное выше это переменные объекта класса
#переменные класса - новые переменные для нас

class Rectngle():

    recs = []

    def __init__(self,w1,l1):
        self.width1 = w1
        self.len1 = l1
        self.recs.append((self.width1,self.len1))

    def print_size(self):
        print("""{} на {}""".format(self.width1,self.len1))

a1 = Rectngle(23,24)
a2 = Rectngle(25,26)
a3 = Rectngle(27,28)
print(Rectngle.recs)


print("Цикл 2 другие методы")

class Lion:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name
    

lion = Lion("Диллери")
print(lion)

class AlwaysPositive:
    def __init__(self,number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

class Person:
    def __init__(self):
        self.name = 'Джон'

bob = Person()
new_a = bob
print(bob is new_a)

a_bob = Person()
print(bob is a_bob)

print("Заключительно задание")

class P1:
    x1 = 10
    def __init__(self,x):
        self.x1 = x
        
    def met1(self):
        if self.x1 is None:
            print("x является None")
        else:
            print("x не является None")
    def met2(self):
        if x is not None:
            print("X не является None")
        else:
            print("X является None")
a1 = P1(None)
s = a1.met1()















