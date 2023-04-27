#импорт библиотеки
import telebot
#переменная 
token = '6169182983:AAEmDmp5vNZAHsxhVHAVJi9_6aQ0BLXBlpM'
#создаем переменную типа телебот :имея  токен
bot = telebot.TeleBot(token)

#декоратор ,зарегестрировали функцию для всех сообщений типа текст
@bot.message_handler(content_types=['text'])

#функция оброботчик принимает сообщение
def echo(message):
    word = 'Артур'
    string = message.text
    if word in string:
        bot.send_message(message.from_user.id, 'Ба! Знакомые все лица!')

    else:
        bot.send_message(message.from_user.id, message.text)



    
# функция постоянно обращающаяся к сервирам
bot.polling(none_stop = True)
