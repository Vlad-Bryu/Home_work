from telegram.ext import Updater, CommandHandler
import ephem
import datetime

PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    update.message.reply_text("Введите /planet {Название планеты} и дату в формате yyyy/mm/dd")


def coordinate_of_planet(bot, update):
    user_text = update.message.text.split()
    now = datetime.datetime.now()
    #date = update.message.date
    if user_text[3] == datetime.strptime(user_text[3], '%Y/%m/%d'):
        coord_planet = getattr(ephem, user_text[1])(user_text[2])
        coordinate = ephem.constellation(coord_planet)
        print(coordinate)
        update.message.reply_text("{} расположен/а в созвездии {} на {}".format(user_text[1], coordinate, user_text[2]))
    else:
        now = datetime.datetime.now()
        coord_planet = getattr(ephem, user_text[1])(now.strftime("%Y/%m/%d"))
        coordinate = ephem.constellation(coord_planet)
        print(coordinate)
        update.message.reply_text("{} расположен/а в созвездии {} на {}".format(user_text[1], coordinate, now.strftime("%Y/%m/%d")))


def main():
    mybot = Updater("887214896:AAHL-ZGnq7zqCXV-k-0dB48iep-HQUzEfW4", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", coordinate_of_planet))

    mybot.start_polling()
    mybot.idle()


main()

