import os
import csv
print("Задание 1")
with open("newfile","r") as r:
    d = r.read()
    print(d)

print("Задание 2")
r1 = input("Введите слово")
st = open("st.txt","w")
s = st.write(r1)
print(s)

with open("newfile","w") as r:
    r.write(r1)


print("задание 3")
list1 = [["Звездные войны","Терминатор","Искуственный интеллект"],["Дурак","Матрица","Левиафан"],["Люди в черном","Я - РОБОТ","Эволюция"]]
list2 = []
print(list2)
for i in list1:
    r = i
with open("new_csv.csv","w") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(list1)
    
