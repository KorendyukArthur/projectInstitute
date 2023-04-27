import math

print("задание 1")
class Apple:
    def __init__(self,w,c,she,vk):
        self.weight = w
        self.color = c
        self.sher = she
        self.vks = vk
        print("переменные созданы")

a1 = Apple(100,"зеленый",50,20)
print(a1.weight)

print("задание 2")

class Circle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a +self.b * math.pi
        

a2 = Circle(3,4)
print(a2.area())

print("Задание 3")

class Triangle:
    def __init__(self,a1,b1,c1):
        self.a = a1
        self.b = b1
        self.c = c1
    def area(self):
        p = (self.a+self.b+self.c)/2
        s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return s

a3 = Triangle(4,5,6)
print(a3.area())

print("Задание 4")
class Hexagon:
    def __init__(self,a1,a2,a3,a4,a5,a6):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        
    def calculate_perimeter(self):
        p = self.a1 + self.a2 + self.a3 + self.a4 + self.a5 + self.a6
        print(p)
    
a4 = Hexagon(1,2,3,4,5,6)
a4.calculate_perimeter()









    
