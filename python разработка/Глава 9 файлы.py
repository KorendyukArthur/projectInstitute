import os
import csv
import тест1

тест1.new_vopros()
d = os.path.join("Users","dsd","tres.text")
print(d)

st = open("st.txt","w")
st.write("Создание файла")
st.close()


my_list = list()
my_list1 = list()

with open("st.txt","r") as new_p:
    print(new_p.read())



with open("newfile.txt","r") as peremenn:
    d1 = peremenn.read()
    my_list.append(d1)
    print(my_list)
with open("newfile.txt","r") as new_go:
    d2 = new_go.read()
    my_list1.append(d2)
print(my_list)
print(my_list1)

with open("stre.csv","w") as f:
    de1 = csv.writer(f, delimiter = ",")
    de1.writerow(["1","2","3"])
    de1.writerow(["4","5","6"])

with open("stre.csv","r") as f1:
    new_de1 = csv.reader(f1,delimiter = ",")
    for new_per in new_de1:
        print(",".join(new_per))


        
