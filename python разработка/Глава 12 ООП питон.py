print("процедурный подход")
print("все действия выполняются последовательно")
print("например")
x = 2
y = 4
z = 9
xyz = x + y * z
print(xyz)

print("Новый пример")
rock = []
country = []
def collect_song():
    song = "Введите песню"
    ask = "Введите р (рок) или к ( кантри). Введите Х для выхода"

    while True:
        genre = input (ask)
        if genre == "X":
            break
        if genre == "р":
            rk = input(song)
            rock.append(rk)

        elif genre == "к":
            kon = input(song)
            country.append(kon)
        else:
            print("Данные не верны.")
    print(rock)
    print(country)
#collect_song()

print("Пример 2")

def increment(a):
    return a+1
print(increment(24))
#резульатом будет 25



