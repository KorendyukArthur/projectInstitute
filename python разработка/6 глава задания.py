print("Практика по 6 главе строки")
print('задание 1')
i = "Чехов"
i1 = i[0]
i2 = i[1]
i3 = i[2]
i4 = i[3]
i5 = i[4]
print(i1)
print(i2)
print(i3)
print(i4)
print(i5)
print("задание 2")
s1 = input()
s2 = input()
si1 = "Вчера я написал {}. Вчера я ходил в {}".format(s1,s2)
print(si1)
print("задание 3")
si2 = "олдос Хексли родился в 1894 году.".capitalize()
print(si2)

print("задание 4")
si3 = "Кто-это? Где это? Когда это?".split("?")
print(si3)

print("задание 5")
listd = ["Рыжая","лиса","перепрыгнула","через","низкий","забор","."]
newlistd = " ".join(listd)
print(newlistd)
listd1 = newlistd.replace("р .", "р.")
print(listd1)

print("задание 6")
t1 = "Ребенок - зеркало поступков родителей."
st1 = t1.replace("о","0")
print(st1)

print("задание 7")
st2 = "хеменгуэй"
stt2 = st2.index("м")
print(stt2)

print("задание 8")

a = "\"прнивет джон\"\"привет Мери\" \"как твои дела\""
print(a)

print("задание 9")
a1 = "три" * 3
print(a1)

a2 = "три" + "три" + "три"
print(a2)


print("Задание 10")

a3 = "И незачем так орать! Я и в первый раз прекрасно слышал."
a12 = a3[0:21]
print(a12)





















