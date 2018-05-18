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
         {'planet':'Сатурн'}, {'planet':'Нептун'}, {'planet':'Плутон'}, {'planet':'Луна' }, {'planet': 'Солнце'}]

constellations = {'Capricornus':'Козерог', 'Gemini': 'Близнецы', 'Aries':'Овен', 'Libra':'Весы',
                  'Sagittarius': 'Стрелец', 'Taurus':'Телец', 'Aquarius': 'Водолей', 'Cancer' : 'Рак',
                  'Leo':'Лев', 'Virgo':'Дева', 'Scorpio': 'Скорпион', 'Pisces': 'Рыбы'}
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
    while True:
        update.message.reply_text('Введите название планеты с большой буквы, для выхода введите: "Выход"\n')
        if update.message.text() != 'Выход':
            solar_system(bot, update)
        elif update.message.text() == 'Выход':
            update.message.reply_text('Выхода нет')


def solar_system(bot, update):

    for objects in solar:
        if objects['planet'] == update.message.text:
            if update.message.text == 'Марс':
                mars = ephem.Mars(sysdate)
                ma = ephem.constellation(mars)[1]
                if ma in constellations:
                    update.message.reply_text(constellations.get(ma))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Юпитер':
                jupiter = ephem.Jupiter(sysdate)
                ju = ephem.constellation(jupiter)[1]
                if ju in constellations:
                    update.message.reply_text(constellations.get(ju))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Луна':
                moon = ephem.Moon(sysdate)
                mo = ephem.constellation(moon)[1]
                if mo in constellations:
                    update.message.reply_text(constellations.get(mo))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Сатурн':
                saturn = ephem.Saturn(sysdate)
                sa = ephem.constellation(saturn)[1]
                if sa in constellations:
                    update.message.reply_text(constellations.get(sa))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Венера':
                venus = ephem.Venus(sysdate)
                ve = ephem.constellation(venus)[1]
                if ve in constellations:
                    update.message.reply_text(constellations.get(ve))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Солнце':
                sun = ephem.Sun(sysdate)
                sa = ephem.constellation(sun)[1]
                if sa in constellations:
                    update.message.reply_text(constellations.get(sa))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Меркурий':
                mercury = ephem.Mercury(sysdate)
                me = ephem.constellation(mercury)[1]
                if me in constellations:
                    update.message.reply_text(constellations.get(me))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Нептун':
                neptune = ephem.Neptune(sysdate)
                ne = ephem.constellation(neptune)[1]
                if ne in constellations:
                    update.message.reply_text(constellations.get(ne))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Плутон':
                update.message.reply_text('Настолько маленькая, что и планетой назвать нельзя')
            else:
                update.message.reply_text('Планету украли')





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