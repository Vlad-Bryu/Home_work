from telegram.ext import Updater, CommandHandler
import ephem
import datetime



PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    update.message.reply_text("Введите /planet {Название планеты} и дату в формате yyyy/mm/dd.")


def coordinate_of_planet(bot, update):
    user_text = update.message.text.split()
    try:
        datetime.datetime.strptime(user_text[2], '%Y/%m/%d')
        coord_planet = getattr(ephem, user_text[1].lower().capitalize())(user_text[2])
        coordinate = ephem.constellation(coord_planet)
        print(coordinate)
        update.message.reply_text("{} расположен/а в созвездии {} на {}".format(user_text[1].lower().capitalize(), coordinate, user_text[2]))
    except IndexError:
        try:
            now = datetime.datetime.now()
            coord_planet = getattr(ephem, user_text[1].lower().capitalize())(now.strftime("%Y/%m/%d"))
            coordinate = ephem.constellation(coord_planet)
            print(coordinate)
            update.message.reply_text("{} расположен/а в созвездии {} на {}".format(user_text[1].lower().capitalize(), coordinate, now.strftime("%Y/%m/%d")))
        except (IndexError, AttributeError):
            update.message.reply_text("Вам необходимо ввести планету")
    except ValueError:
            update.message.reply_text("Введите запрос в таком формате: /planet Nameplanet(Mars) YYYY/mm/dd")

def main():
    mybot = Updater("887214896:AAHL-ZGnq7zqCXV-k-0dB48iep-HQUzEfW4", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", coordinate_of_planet))

    mybot.start_polling()
    mybot.idle()


main()

