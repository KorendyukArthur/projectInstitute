
def count_characters(string):
    lis = {}
    string = string.lower()
    for i in string:
        if i in lis:
            lis[i] +=1
        else:
            lis[i] = 1
    print(lis)
    

count_characters("привет как твои дела ")

#Рекурсия

def bootles_of_beer(bob):
    if bob < 1:
        print("dewed")
        return
    tmp = bob
    bob -=1
    print("{} on {} tw {} th  ".format(tmp,tmp,bob))
    bootles_of_beer(bob)

bootles_of_beer(5)
