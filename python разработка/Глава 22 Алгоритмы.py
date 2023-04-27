#программа для вывода чисел от 1 до 100.
#Но вместо чисел кратных трем выводит Физз
#Вместо чисел кратных пяти выводит Базз
#Вместо кратных трем и пяти фаннбазз

#Решение задания
def funbaz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("Funbazz")
        else:
            if i % 3 == 0:
                print("fun")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)
funbaz()
        
#Последовательный поиск

def pospois(number_list,N):
    found = False
    for i in number_list:
        if i == N:
            found = True
            break
    return found

number = range(0,100)
o1 = pospois(number,3)
print(o1)

#последовательный поиск
def func1(number_list,chislo):
    chist = False

    for i in number_list:
        if i == chislo:
            chist = True
            break
    return chist

number = range(1,200)
o2 = func1(number,240)
print(o2)

def func2(number_list3,number):
    const = False
    for i in number_list3:
        if i == number:
            const = True
            break
    return const

nu = range(1,1000)
ot1 = func2(nu,999)
print(ot1)



def func3(num_spis,number):
    x = False
    for i in num_spis:
        if i >= number and i <= 100:
            x = True
            print("Элемент найден")
    return x

a11 = range(80,120)
o12 = func3(a11,85)
print(o12)

def func5(numb_list,num_srav):
    const = False
    for i in numb_list:
        if i == num_srav:
            const = True
            break
    return const
s = range(1,100)
print(func5(s,50))

    
    
def func6():
    for i in range(1,100):
        if i % 3 == 0  and i % 5 == 0:
            print("funbaz")
        elif i % 3 == 0:
            print("fun")
        elif i % 5 == 0:
            print("buz")
        else:
            print(i)

s = func6()
print(s)


def func8():
    i = "Привет"
    #i = i.lower()
    return i[::-1]


print(func8())



def func9():
    i1 = "сон"
    return i1[::-1]
print(func9())



def sa(num_lis,num):
    s = False
    for i in num_lis:
        if i == num:
            s = True
            break
    return s
n_l = range(1,30)
print(sa(n_l,40))


#Полиндром - слово которое записывается в обоих направлениях одинаково

def polindrome(word):
    word = word.lower()
    return word[::-1] == word

print(polindrome("Сергей"))
print(polindrome("АВА"))


def new_pol(word):
    word = word.lower()
    return word[::-1] == word
print(new_pol("Авак"))

#Анаграмма
print("Анаграмма")
def func12(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(func12("арага","гара"))

#Подсчет вхождений в словарь

def func13(string):
    count_dict = {}
    for i in string:
        if i in count_dict:
            count_dict[i] +=1
        else:
            count_dict[i] = 1
    print(count_dict)

print(func13("Агрессия"))
        


































            
