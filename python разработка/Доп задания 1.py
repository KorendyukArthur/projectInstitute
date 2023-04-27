#Задание1
def func():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    for i in a:
        if i <= 5:
            print(i)
print(func())

#Задание2
def func1():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)

    print(c)

print(func1())


#Задание3

#Задание4
def func2():
    dict1 = {1:10, 2:20}
    dict2 = {3:30, 4:40}
    dict3 = {5:50, 6:60}
    result = {}
    for i in (dict1, dict2, dict3):
        result.update(i)
    print(result)

print(func2())

#Задание5

def func3():
    my_dict = {'a':500,'b':5874,'c':560,'d':400,'e':5874,'f':20}
    count = 0
    my_dict1 = {}
    while count <= 4:
        max_val = max(my_dict.values())
        print(max_val)
        del max_val[max(max_val,key=max_val.get)]

print(func3())







    
