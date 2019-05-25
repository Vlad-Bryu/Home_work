from telegram.ext import Updater, CommandHandler
import ephem

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



def greet_user(bot, update):
    text = 'Доступна команда /planet (показывает в каком созвездии находится планета в текущий момент)'
    print(text)


def coordinate_of_planet(bot, update):
    def func():
        user_text = update.message.text.split()
        #date = update.message.date.split(' ')
        #print(date)
        print(len(user_text))
        return user_text[1]
    coord_planet = ephem.func()('2018/01/01')
    coordinate = ephem.constellation(coord_planet)
    print(coordinate)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text="{planet} в созвездии {coordinate} на 2018/01/01".format(planet=planet,
                                                                                  coordinate=coordinate
                                                                                ))


def main():
    mybot = Updater("887214896:AAHL-ZGnq7zqCXV-k-0dB48iep-HQUzEfW4", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", coordinate_of_planet))

    mybot.start_polling()
    mybot.idle()


main()

