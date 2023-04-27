
import random

HELP = ''' help - напечатать справку по программе.
            add - добавить задачу в список(название задачи запрашивать у пользователя
            show - напечатать все добавленные задачи
            random - добавляет случ. задачу на дату сегодня
            '''

today = []
tomorrow = []
other = []
tasks = {}

RANDOM_TASK = ['Повторить ООП','Покормить кота','Написать сайт',
               'Разобраться в домашних делах','Позвонить по квартире']

def add_gogo(date,task):
    if date in tasks:
        
        tasks[date].append(task)
        print("задача",task,'добавлена по дате', date)

    else:
        tasks[date] = []
        tasks[date].append(task)
        print("задача",task,'добавлена по дате', date)
run = True


while run:
    command = input("Введите команду: ")
    if command == 'help':    
        print(HELP)

        
    elif command == 'show':
        date = input("Введите дату для отображения задач")
        if date in tasks:
            for task in tasks[date]:
                print('- ',task)
        else:
            print('такой даты нет')

    elif command == 'random':
        task = random.choice(RANDOM_TASK)
        add_gogo('Сегодня',task)
        
    elif command == 'add':
        date = input("Введите дату выполнения задачи: ")
        task = input("Введите название задачи")
        add_gogo(date,task)
    else:
        print("неизвестная задача")
        break
print("До свидания")
