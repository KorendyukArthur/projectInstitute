def newpabg():
    n = input("Введите чило: ")
    n = int(n)
    c = int(input("Введите еще число: "))
    if n%2==0:
        print("четное")
    else:
        print("Нечетное")
        newC = (c + n) * 32
        print(newC)

newpabg()


def newdeli(s,e):
        if s >= e:
            for i in range(4):
              e = s + 5 + 5
              print(e)
        else:
            print(s)
            print(e)

newdeli(3,4)
print("новое значение")
newdeli(6,3)


#показание датчиков здоровья и улучшение репутациb
def ar1():
    x = int(input())
    y = int(45)
    if x >= 90:
        print("здоровье на максимуме")
        x = int(x)
        y += 1
        print("репутация улучшилась")
        print("y:", y)
        a = str("деньги за новые задания увеличились до ставки в")
        ar = len(a)
        print(ar)
                
    elif x <=90 and x>= 45:
        print("Хорошие новости, среднее здоровье")
        b = str("деньги за новые задания составляют")
        ar = len(b)
        print(ar)
        
    else:
        print("плохие новости здоровье упало")
        y -= 1
        print("репутация мин")
        c = str("репутация мин деньги мин")
        print("y:", y )
        ar = len (c)
        print(ar)
ar1()
ar1()



    











        
