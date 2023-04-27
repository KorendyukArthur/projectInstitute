'''файл для повторения'''

'''создание функции'''
def namefunc(x,y,z=4):
    return x+y+z

n1 = namefunc(4,5)
n2 = namefunc(1,1)

test_pr1 = int(input())
test_pr2 = int(input())
if test_pr1 >= test_pr2:
    print (n1)
elif test_pr2 <= test_pr2:
    print (n2)
else:
    print ("исключение")

    
test_pr3 = "4"

for i in range(3):
    print(test_pr3)



'''написать словарь при вводе ключа показывается значение'''

dict1 = {}
dict1["1"] = "стул"
dict1["2"] = "стол"
dict1["3"] = "дверь"
dict1["4"] = "конистра"

a1 = input()
if a1 in dict1:
    a2 = dict1[a1]
    print(a2)
else:
    print("значения нет")

dict2 = dict()
dict2["5"] = "фурнитура"
dict2["6"] = "крышка"
dict2["7"] = "ложка"
dict2["8"] = "скатерть"
dict2["9"] = "ножик"

chislo1  = input()
if chislo1 in dict2:
    ch1 = dict2[chislo1]
    print(ch1)
else:
    print("ошибка")




































    
