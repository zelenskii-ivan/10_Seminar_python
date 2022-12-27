import requests
import telebot
import json

bot = telebot.TeleBot("5787925817:AAE0PJWskvP14Gv7uw_5uI44ObbJQS6Yqbc")
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот курс валют.\nКоманда /USD для доллара США. "
                          "\nКоманда /EUR для Евро.")


@bot.message_handler(commands=['USD'])
def send_welcome(message):
    var = res['Valute']['USD']['Value']
    bot.reply_to(message, f'Курс доллара: {var}')


@bot.message_handler(commands=['EUR'])
def send_welcome(message):
    var = res['Valute']['EUR']['Value']
    bot.reply_to(message, f'Курс евро: {var}')


bot.infinity_polling()