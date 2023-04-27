s = "Это был прекрасный день. В январскую пору мы сидели в корете. Как же красив день! О это превосходно"
s1 = s.split(".")
print(s1)
i1 = "день"
s2 = "Какой прекрасный {}"
s3 = s2.format(i1)
print(s3)

print("метод join добавление между строк")

s4 = "до.ре.ми"
o1 = "+".join(s4)
print(o1)

s5 = ["1","2","3","4"]
o2 = "".join(s5)
print(o2)
o3 = " ".join(s5)
print(o3)
o4 = "вот:".join(s5)
print(o4)

print("метода strip - метод удаления пробелов в начале и в конце")
s6 = "     три человека    "
o5 = s6.strip()
print(o5)

print("метод replace - земеняет символ( вхождение) в строке на то что вы захотите")
s7 = s.replace("е","1")
print(s7)

s8 = s.replace("день","пень")
print(s8)

print("метод index - используется для поиска первого вхождения элменета")
s9 = s.index("у")
print(s9)

s10 = s.index("день")
print(s10)

try:
   s11 = s.index("лень")
   print(s11)
except:
    print("не найдено")


i = "карета" in s
print(i)

d = "день" in s
print(d)

d1 = s.replace(" ","\n")
print(d1)

d2 = "строка1\nстрока2\nстрока3\n"
print(d2)

o11 = s5[2:3]
print(o11)




