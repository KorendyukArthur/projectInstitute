print("Глава 12 ООП питон чтость 2")
class Orange:
    def __init__(self):
        print("Метод создан!")

print("Объявление переменной метода")
class Orange1:
    def __init__(self, w, c):
        
        self.weight = w
        self.color = c
        print("Созданы переменне!")


orl1 = Orange1(10,"темный апельсин")
print(orl1)


orl2 = Orange()
print(orl2)

print(orl1.color)
print(orl1.weight)

class NewClass1:
    def __init__(self, w, c, d, sh):
        self.weight1 = w
        self.color1 = c
        self.dlin1 = d
        self.sher1 = sh
        print("Переменные созданы")

sa1 = NewClass1(11, "белый", 150, 40)
print(sa1)

print("Вывод значений переменных")
print(sa1.weight1)


print("изменение переменной объекта")

s = NewClass1.weight1 = 100
print(s)
print(NewClass1.weight1)


sa2 = NewClass1(50,"синий",100,60)
sa3 = NewClass1(60,"серый",90,60)
sa4 = NewClass1(70,"Оранжевый",99,46)



class Orange2:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Переменные класса Orange2 созданы")
    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange2(6,"мандарин")
print(orange.mold)
orange.rot(10,3)
print(orange.mold)

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
        print("переменные созданы")

    def area(self):
        return self.width * self.len
        print("Расчет выполнен")

    def change_size(self, w, l):
        self.width = w
        self.len = l
        print("размер изменен")


newRest = Rectangle(100,500)
newRest1 = Rectangle(200,500)

print(newRest.area())
print(newRest1.area())

print("Применение метода change_size")
newRest.change_size(2,10)
print(newRest.area())
newRest1.change_size(5,20)
print(newRest1.area())











    
        






