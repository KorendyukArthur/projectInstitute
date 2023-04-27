newspisc = list()
newspisc.append("товар один")
newspisc.append("товар два")
newspisc.append("товар три")
print(newspisc)
a = newspisc[1]
print(a)
newspisc[0] = "нет товара"
print(newspisc)
newspisc[0] = "товар один"
print(newspisc)
b = newspisc.pop()
print(newspisc)
newspisc.append("товар четыре")
print(newspisc)
newspisc[2] = ("товар три")
print(newspisc)

spisc2 = []
spisc2.append("Стул")
spisc2.append("стул")
spisc2.append("столешница")
spisc2.append("скатерть")
print(spisc2)
spisc2.pop()
spisc2[2] = "шкаф"
print(spisc2)
c = spisc2 + newspisc
print(c)

test1 = "шкаф" in c
print(test1)

test2 = "скатерть" in c
print(test2)

test3 = "шкафы" not in c
print(test3)

test4 = "Стул" not in newspisc
print(test4)

test5 = len(c)
print(test5)

''' пример программы списков'''
modcar = []
modcar.append("VW")
modcar.append("BMW")
modcar.append("AUDI")
modcar.append("SEAT")
mail = input("введите марку авто из четврех, бмв,ауди, фв,сеат:")
if mail in modcar:
    print("введено верно")
else:
    print("неверно")


'''новая тестовая программа для работы списков'''

def plusod(x = 1):
    return x + 20
lis = ["один","два","три"]
maiil1 = int(input("Введите число для поиска слов:"))
maiil = plusod() + maiil1
if maiil >= 10 and maiil <= 50:
    lis[0] = "плюс"
    print(lis)
elif maiil <= 10:
    lis[1] = "минус"
    print(lis)
else:
    b1 = len(lis)
    print(b1)




    
    
    









