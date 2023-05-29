import datetime
import telegram
from telegram.ext import Updater, CommandHandler
import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('API_TOKEN')
bot_token = os.getenv('TELEGRAM_TOKEN')

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Введіть /jaka_para щоб отримати посилання на пару.'
                                                                  '\nІнші команди:'
                                                                  '\n/next_para'
                                                                  '\n/smishunka'
                                                                  '\n/history')

def jaka_para(n, update, context):
    current_time = float(datetime.datetime.now().strftime("%H.%M")) + n
    day_of_week = datetime.datetime.today().strftime("%A")
    day = datetime.datetime.today().day
    month = datetime.datetime.today().month

    if n == 4.5:
        context.bot.send_message(chat_id=update.message.chat_id, text="Наступна пара:")

    if day_of_week == "Monday":

        if 7.00 <= current_time <= 9.55:
            text="Дискретна математика (Лекція) 😐 8:30 - 10:05\nhttps://us02web.zoom.us/j/87578307057?pwd=UGwyVGlwc3M4Q0Q0Q0NLWUt6bmVpUT09"
        elif 9.55 <= current_time <= 11.50:
            text="Комп'ютерна логіка (Лекція) 😐 10:25 - 12:00\nhttps://bbb.comsys.kpi.ua/b/val-2vb-o7w-y5y"
        elif 11.50 <= current_time <= 13.45:
            if (day+month)% 2 == 0:
                text = "Культура мовлення (Лекція) 😊 12:20 - 13:55\nhttps://bbb.comsys.kpi.ua/b/myk-0iw-red-p01"
            else:
                text="Вища математика (Лекція) 😬 12:20 - 13:55\nhttps://us04web.zoom.us/j/2684350438?pwd=kiOi3BrgbJHeYvkrx7qaSxa08J8m8O.1"
        else:
            text="Чілим 😴"

    elif day_of_week == "Tuesday":

        if 7.00 <= current_time <= 9.55:
            text = "Основи здорового способу життя 😊 8:30 - 10:05\nhttps://us05web.zoom.us/j/7875142930?pwd=N0NwbUNBOXVCZ1YybWtpOEMvampwQT09"
        elif 9.55 <= current_time <= 11.50:
            text = "Практичний курс іноземної мови 😐 10:25 - 12:00\nhttps://meet.google.com/bwg-pdnr-evh"
        elif 11.50 <= current_time <= 13.45:
            text = "Вища математика (Практика) 😊 12:20 - 13:55\nhttps://us04web.zoom.us/j/2313886209?pwd=dnZHanV3cU9LUXJBVWYyYVArUFg5dz09"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Wednesday":

        if 12.00 <= current_time <= 13.45:
            text = "Фізика (Лабораторна) 12:20 - 13:55"
        elif 13.45 <= current_time <= 15.40:
            if (day + month) % 2 == 0:
                text = "Культура мовлення (Практика) 😊 14:15 - 15:50\nhttps://bbb.comsys.kpi.ua/b/myk-0iw-red-p01"
            else:
                text = "Чілим 😴"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Thursday":

        if 9.55 <= current_time <= 11.50:
            text = "Вища математика (Лекція) 😬 10:25 - 12:00\nhttps://us04web.zoom.us/j/2684350438?pwd=kiOi3BrgbJHeYvkrx7qaSxa08J8m8O.1"
        elif 11.50 <= current_time <= 13.45:
            text = "Фізика (Лекція) 😬 12:20 - 13:55\nhttps://meet.google.com/ivm-vfpz-ugo"
        elif 13.45 <= current_time <= 15.40:
            text = "Програмування (Лекція) 😊 14:15 - 15:50\nhttps://us02web.zoom.us/j/2711546637?pwd=Ry82RHp3SjV6WTZRMXl6WUNod25hUT09"
        else:
            text = "Чілим 😴"

    elif day_of_week == "Friday":

        if 9.55 <= current_time <= 11.50:
            if (day + month) % 2 == 0:
                text = "Дискретна математика (Лабораторна) 😐 10:25 - 12:00\nhttps://us05web.zoom.us/j/7089075754?pwd=TWRlZmxyVlFiTWU1UGlVVU1XcFE0Zz09"
            else:
                text = "Програмування (Практика) 😊 10:25 - 12:00\nhttps://us02web.zoom.us/j/2711546637?pwd=Ry82RHp3SjV6WTZRMXl6WUNod25hUT09"
        elif 11.50 <= current_time <= 13.45:
            if (day + month) % 2 == 0:
                text = "Вища математика (Практика) 😊 12:20 - 13:55\nhttps://us05web.zoom.us/j/81227675458?pwd=SWFuQTZLY2w5a2dMMjd0cTdxSUN6dz09"
            else:
                text = "Комп'ютерна логіка (Лабораторна) 😐 12:20 - 13:55\nhttps://us04web.zoom.us/j/7382214783?pwd=RnZ3SWgwK1JoVkZtNndnKzdPZjFGdz09"
        elif 13.45 <= current_time <= 15.40:
            text = "Фізика (Практика) 😬 14:15 - 15:50\nhttps://meet.google.com/ivm-vfpz-ugo"
        else:
            text = "Чілим 😴"

    else:
        text="Чілим 😴"

    context.bot.send_message(chat_id=update.message.chat_id, text=text)

def get_result_from_chat_gpt(text: str):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "assistant" ,"content": text}],
        temperature = 0.8,
        max_tokens = 1500,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
    )
    return response['choices'][0]['message']['content']

def get_image_from_dall_e(prompt: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )
    return response["data"][0]["url"]

def smishunka(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Смішний ChatGPT:\n")
    text = get_result_from_chat_gpt("Українською мовою, 1-3 речення, придамай дуже смішний анекдот")
    context.bot.send_message(chat_id=update.message.chat_id,text=text)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=get_image_from_dall_e(text))

def history(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Історія від ChatGPT:\n")
    text = get_result_from_chat_gpt("Напишіть розповідь з 5-6 речень українською мовою.")
    context.bot.send_message(chat_id=update.message.chat_id,text=text)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=get_image_from_dall_e(text))

bot = telegram.Bot(token=bot_token)
updater = Updater(bot_token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('jaka_para', lambda update, context: jaka_para(3, update, context)))
dispatcher.add_handler(CommandHandler('next_para', lambda update, context: jaka_para(4.5, update, context)))
dispatcher.add_handler(CommandHandler('smishunka', smishunka))
dispatcher.add_handler(CommandHandler('history', history))

updater.start_polling()