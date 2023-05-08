import datetime
import telegram
from telegram.ext import Updater, CommandHandler

bot_token = '6052645146:AAF_T-kpgMBSnyAvUbddYyf2xkNX93MLlAo'


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Введіть /jaka_para щоб отримати посилання на пару')

# Функція-відповідь на команду /jaka_para
def jaka_para(update, context):
    current_time = float(datetime.datetime.now().strftime("%H.%M")) + 3
    day_of_week = datetime.datetime.today().strftime("%A")
    day = datetime.datetime.today().day
    month = datetime.datetime.today().month

    # context.bot.send_message(chat_id=update.message.chat_id, text=current_time)
    # context.bot.send_message(chat_id=update.message.chat_id, text=day_of_week)
    # ontext.bot.send_message(chat_id=update.message.chat_id, text=day)

    if day_of_week == "Monday":

        if current_time >= 7.00 and current_time <= 9.55:
            text="Дискретна математика (Лекція) 😐 8:30\nhttps://us02web.zoom.us/j/87578307057?pwd=UGwyVGlwc3M4Q0Q0Q0NLWUt6bmVpUT09"
        elif current_time >= 9.55 and current_time <= 11.50:
            text="Комп'ютерна логіка (Лекція) 😐 10:25\nhttps://bbb.comsys.kpi.ua/b/val-2vb-o7w-y5y"
        elif current_time >= 11.50 and current_time <= 13.45:
            if (day+month)% 2 == 0:
                text = "Культура мовлення (Лекція) 😊 12:20\nhttps://bbb.comsys.kpi.ua/b/myk-0iw-red-p01"
            else:
                text="Вища математика (Лекція) 😬 12:20\nhttps://us04web.zoom.us/j/2684350438?pwd=kiOi3BrgbJHeYvkrx7qaSxa08J8m8O.1"
        else:
            text="Чілим 😴"

    elif day_of_week == "Tuesday":

        if current_time >= 7.00 and current_time <= 9.55:
            text = "Основи здорового способу життя 😊 8:30\nhttps://us05web.zoom.us/j/7875142930?pwd=N0NwbUNBOXVCZ1YybWtpOEMvampwQT09"
        elif current_time >= 9.55 and current_time <= 11.50:
            text = "Практичний курс іноземної мови 😐 10:25\nhttps://meet.google.com/bwg-pdnr-evh"
        elif current_time >= 11.50 and current_time <= 13.45:
            text = "Вища математика (Практика) 😊 12:20\nhttps://us04web.zoom.us/j/2313886209?pwd=dnZHanV3cU9LUXJBVWYyYVArUFg5dz09"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Wednesday":

        if current_time >= 12.00 and current_time <= 13.45:
            text = "Фізика (Лабораторна) 12:20"
        elif current_time >= 13.45 and current_time <= 15.40:
            if (day + month) % 2 == 0:
                text = "Культура мовлення (Практика) 😊 14:15\nhttps://bbb.comsys.kpi.ua/b/myk-0iw-red-p01"
            else:
                text = "Чілим 😴"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Thursday":

        if current_time >= 9.55 and current_time <= 11.50:
            text = "Вища математика (Лекція) 😬 10:25\nhttps://us04web.zoom.us/j/2684350438?pwd=kiOi3BrgbJHeYvkrx7qaSxa08J8m8O.1"
        elif current_time >= 11.50 and current_time <= 13.45:
            text = "Фізика (Лекція) 😬 12:20\nА посилання Русаков знову забув скинути"
        elif current_time >= 13.45 and current_time <= 15.40:
            text = "Програмування (Лекція) 😊 14:15\nhttps://us02web.zoom.us/j/2711546637?pwd=Ry82RHp3SjV6WTZRMXl6WUNod25hUT09"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Friday":

        if current_time >= 9.55 and current_time <= 11.50:
            if (day + month) % 2 == 0:
                text = "Дискретна математика (Лабораторна) 😐 10:25\nhttps://us05web.zoom.us/j/7089075754?pwd=TWRlZmxyVlFiTWU1UGlVVU1XcFE0Zz09"
            else:
                text = "Програмування (Практика) 😊 10:25\nhttps://us02web.zoom.us/j/2711546637?pwd=Ry82RHp3SjV6WTZRMXl6WUNod25hUT09"
        elif current_time >= 11.50 and current_time <= 13.45:
            if (day + month) % 2 == 0:
                text = "Вища математика (Практика) 😊 12:20\nhttps://us05web.zoom.us/j/81227675458?pwd=SWFuQTZLY2w5a2dMMjd0cTdxSUN6dz09"
            else:
                text = "Комп'ютерна логіка (Лабораторна) 😐 12:20\nА посилання Русаков знову забув скинути"
        elif current_time >= 13.45 and current_time <= 15.40:
            text = "Фізика (Практика) 😬 14:15\nhttps://meet.google.com/ivm-vfpz-ugo"
        else:
            text = "Чілим 😴"

    else:
        text="Чілим 😴"

    context.bot.send_message(chat_id=update.message.chat_id, text=text)

# Ініціалізація об'єкту бота та диспетчера
bot = telegram.Bot(token=bot_token)
updater = Updater(bot_token)
dispatcher = updater.dispatcher

# створюємо обробник команди "/start"
dispatcher.add_handler(CommandHandler('start', start))

# Додавання обробника команди /jaka_para
dispatcher.add_handler(CommandHandler('jaka_para', jaka_para))

# Запуск бота
updater.start_polling()