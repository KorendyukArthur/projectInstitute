print("Инкапсуляция.первая концепция")
class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def area(self):
        return self.width * self.len
a1 = Rectangle(3,4)
print(a1.area())

print("Инкапсуляция.вторая концепция")
class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n
        print(n)
        print(self.nums)

a2 = Data()
a2.change_data(3,2)

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)
print("закрытые переменные должны начинаться с _ например _new_perem")

print("""Абстракция - процесс отнятия или удаления у чего - то характеристик
    с целью сведения кго к набору основных, существенных характеристик""")
print("""У человека есть множество характеристик, но мы можем некоторые
из этих данных опустить. Примером абстракции можеть быть создание класса
с опущением некоторых свойств человека. Объекты которые создает класс,
являются абстракциями людей
""")
print("Пример")
class Person():
    def __init__(self,w,d,c):
        self.weight = w
        self.dlin = d
        self.eat = 0
        self.color = c
    def eat1(self):
        for i in range(1,5):
            self.eat += 1
        return self.eat
a3 = Person(1,2,3)
print(a3.eat1())

print("Полиморфизм")
print("""Полиморфизм - способность представлять один и тот же интерфейс
для разных базовых форм""")
print("Пример")
print("Привет мир!")
print(200)
print(200.1)
tr1 = 0
sw1 = 0
cr1 = 0
shapes = [tr1,sw1,cr1]


print("Наследование")
print("есть родительский класс и дочерний")

class Shape():
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {}""".format(self.width,self.len))

my_a1 = Shape(3,4)
my_a1.print_size()


class Square(Shape):
    pass
ne_my_a1 = Square(20,30)
ne_my_a1.print_size()


print("новый класс")
class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {}""".format(self.width,self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

s = Square(20,40)
print(s.area())


print("Наследование. Переопределение метода")

class Shape():
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def print_size(self):
        print("{} by {} ".fromat(self.width,self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("я {} на {}".format(self.width,self.len))

a_sel1 = Square(20,20)
a_sel1.print_size()


print("Композиция.")
#создаем классы для человека и собаки и определяем параметры
class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self,name):
        self.name = name

#Далее создаем объект собаки и передаем в параметр имя хозяина

new_person = Person("Адам Джонс")
new_dog = Dog("Радо","Бульдог",new_person)
print(new_dog.owner.name)

new_person1 = Person("Дик Купер")
new_dog1 = Dog("Сильва","Ротвеллер",new_person1)
print(new_dog1.owner.name)
