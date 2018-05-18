from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime



PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
     'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

#PROXY = {'proxy_url': 'socks5://95.215.54.206:39880'}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
solar = [{'planet':'Меркурий'},{'planet':'Венера'}, {'planet':'Земля'}, {'planet':'Марс'},{'planet': 'Юпитер'},
         {'planet':'Сатурн'}, {'planet':'Нептун'}, {'planet':'Плутон'}, {'planet':'Луна' }]

sysdate = datetime.datetime.now()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    if user_text == 'Привет':
        print(user_text)
        update.message.reply_text('И тебе привет')
    elif user_text == 'Пока':
        print(user_text)
        update.message.reply_text('До новых встреч')

    else:
        print(user_text)
        update.message.reply_text(user_text)


def question(bot, update):
    planets = update.message.reply_text('Введите название планеты с большой буквы, для выхода введите: "Выход"\n')
    if planets != 'Выход':
        solar_system(bot, update)



def solar_system(bot, update):

    for objects in solar:
        if objects['planet'] == update.message.text:
            if update.message.text == 'Марс':
                mars = ephem.Mars(sysdate)
                update.message.reply_text (ephem.constellation(mars))
            elif update.message.text == 'Юпитер':
                jupiter = ephem.Jupiter(sysdate)
                update.message.reply_text (ephem.constellation(jupiter))
            elif update.message.text == 'Луна':
                moon = ephem.Moon(sysdate)
                update.message.reply_text(ephem.constellation(moon))
            elif update.message.text == 'Сатурн':
                saturn = ephem.Saturn(sysdate)
                update.message.reply_text(ephem.constellation(saturn))
            else:
                update.message.reply_text('нет планеты')




def main():
    mybot = Updater("525299103:AAHfha3orrDK7khmGe6GKVKkyBkSAiqK0Zg", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", question))
    dp.add_handler(MessageHandler(Filters.text, solar_system))

    mybot.start_polling()
    mybot.idle()



if __name__ == '__main__':
    main()