a = input("Введите число номер 1:")
b = input("Введите число номер 2:")
c = input("Введите число номер 3:")
try:
    """Необходимо ввести
значения отличные от нуля и типом int
"""
    a=int(a)
    b=int(b)
    print(a/b)
except ZeroDivisionError:
    print("ошибка деления на ноль")
except ValueError:
    print("Ошибка значения")
