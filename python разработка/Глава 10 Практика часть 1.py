
import datetime

def hangman(word):
    list_s1 = ["кот","рот","дот","лот","тор"]
    now = datetime.datetime.now()
    chislo = now.strftime("%H:%M:%S")
    print(chislo)
    chi1= str(chislo)
    r = chi1[7]
    print(r)
    if r <= "2":
        word = "кот"
    elif r >= "2" and r <= "4":
        word = "рот"
    elif r >= "4" and r <= "6":
        word = "дот"
    elif r >= "6" and r <= "8"
    :
        word = "лот"
    else:
        word = "тор"
        
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|        |          ",
              "|        0          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на эту казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Вы выйграли!, загаданное слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Проигрыш, Было загадано слово:{}.".format(word))

hangman(datetime)

    
