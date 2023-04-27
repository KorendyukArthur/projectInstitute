'''практика для пятой главы'''
print("задание 1")
list_music = list()
list_music.append("первый музыкант")
list_music.append("второй музыкант")
list_music.append("третий музыкант")
list_music.append("четвертый музыкант")
print(list_music)
list_music1 = ["один","два","три"]
print(list_music1)

print("задание 2")
new_tuple = ("d: 22 s:33")
new_tuple1 = ("d: 24 s: 44")
new_tuple2 = ("d: 25 s:55")
new_tuple3 = ("d: 33 s:65")
list_life = []
list_life.append(new_tuple)
list_life.append(new_tuple1)
list_life.append(new_tuple2)
list_life.append(new_tuple3)
print(list_life)
s = print(list_life[3])

print("задание 3")
new_slov = {}
new_slov["рост"] = "180"
new_slov["л цвет"] = "красный"
new_slov["л актер"] = "ноу нейм"
print(new_slov)

print("задание 4")
data1 = input()
if data1 in new_slov:
    print(new_slov[data1])
else:
    print("нет данных")

new_slow = {"180":"ваш рост","67":"ваш вес","90":"интеллект"}
i = input()
if i in new_slow:
    print(new_slow[i])
else:
    print("неудача")

print("задание 5")
new_list = ["contry","contry1","country2"]
new_list1 = ["gogo","flesh","ciberenergy"]

slow_new = {}
slow_new["genry"] = new_list
slow_new["garry"] = new_list1
print(slow_new)

i1 = input("введите певца:")
if i1 in slow_new:
    print(slow_new[i1])
else:
    print("ошибка")

print("задание 6")
i3 = input()
def nameq1(i1):
    if i1 in slow_new:
        print(slow_new[i3])
    else:
        print("ошибка")
i2 = nameq1(i3)











