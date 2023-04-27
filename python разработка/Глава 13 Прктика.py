import math
print("Задание 1")

class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
        #периметр круга 2 * пи * р
        #периметр прямоугольника 2*(a+b)
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

class Square():
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r

    def calculate_perimeter(self):
        return 2 * math.pi * self.r

new_1 = Rectangle(2,3)
print(new_1.calculate_perimeter())

new_2 = Square(2,3,4)
print(new_2.calculate_perimeter())

print("Задание 2")

class Shape():   
    def what_am_i(self):
        print("Фигура")

class Rectangle1(Shape):
    def __init__(self,a1,b1):
        self.a1 = a1
        self.b1 = b1

    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

class Square(Shape):
    def __init__(self,a1,b1,r1):
        self.a1 = a1
        self.b1 = b1
        self.r1 = r1

    def calculate_perimeter(self):
        return 2 * math.pi * self.r1 * self.a1

    def change_size(self,dek):
        if  dek >= 0:
            a1 = self.a1 + dek
            a2 = self.b1 + dek
            
        else:
            result1 = self.a1 - dek
            result2 = self.b1 - dek
            print(result1)
            print(result2)

new_obj1 = Square(1,2,3)
print(new_obj1.calculate_perimeter())
new_obj1.change_size(3)
print(new_obj1.calculate_perimeter())


print("Задание 3")
new_a21 = Square(1,2,3)
new_a21.what_am_i()
new_a22 = Rectangle1(1,2)
new_a22.what_am_i()


print("Задание 4")

class Horse():
    def __init__(self,name,color,hes):
        self.name = name
        self.color = color
        self.hes = hes

class Rider():
    def __init__(self,n1):
        self.name1 = n1


obj2 = Rider("Джон")
obj1 = Horse("Дева","Рок",obj2)
s1 = ("{} на лошади {} ".format(obj1.hes.name1,obj1.name))
print(obj1.hes.name1)
print(s1)


obj3 = Rider("Илая")
obj4 = Horse("Ева","черный",obj3)

s1 = ("{} на лошади {} цвет ее {}".format(obj4.hes.name1, obj4.name, obj4.color))
print(s1)







        





















    
