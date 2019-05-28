from telegram.ext import Updater, CommandHandler
import ephem

PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    update.message.reply_text("Доступна команда /planet (показывает в каком созвездии находится планета в текущий момент)")


def coordinate_of_planet(bot, update):
    user_text = update.message.text.split()
    date = update.message.date
    print(date)
    print(len(user_text))
    coord_planet = ephem.user_text[1]('2018/01/01')
    coordinate = ephem.constellation(coord_planet)
    print(coordinate)
    update.message.reply_text("Положение {} в созвездии {}".format(user_text[1], coordinate))


def main():
    mybot = Updater("887214896:AAHL-ZGnq7zqCXV-k-0dB48iep-HQUzEfW4", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", coordinate_of_planet))

    mybot.start_polling()
    mybot.idle()


main()

