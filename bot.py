from cnfg import tokenn
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import requests


bot = telepot.Bot(tokenn)


def on_chat_message(msg):
    command = msg['text'].lower()
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if command == '/rates':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='USD', callback_data='first')],
                [InlineKeyboardButton(text='EUR', callback_data='second')],
                [InlineKeyboardButton(text='GBP', callback_data='third')]

            ])
            bot.sendMessage(chat_id, 'Choose currency', reply_markup=keyboard)
        elif command == '/usd':
            InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='USD', callback_data='first')]])
            url = "https://www.cbr-xml-daily.ru/daily_json.js"
            r = requests.get(url).json()
            f = (r["Valute"]["USD"]["Value"])
            bot.sendMessage(chat_id, f)
            bot.sendMessage(chat_id, 'рублей стоит один доллар')
        elif command == '/eur':
            InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='EUR', callback_data='first')]])
            url = "https://www.cbr-xml-daily.ru/daily_json.js"
            r = requests.get(url).json()
            f = (r["Valute"]["EUR"]["Value"])
            bot.sendMessage(chat_id, f)
            bot.sendMessage(chat_id, 'рублей стоит один евро')
        elif command == '/gbp':
            InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='GBP', callback_data='first')]])
            url = "https://www.cbr-xml-daily.ru/daily_json.js"
            r = requests.get(url).json()
            f = (r["Valute"]["GBP"]["Value"])
            bot.sendMessage(chat_id, f)
            bot.sendMessage(chat_id, 'рублей стоит один фунт')
        elif command == '/start':
            bot.sendMessage(chat_id, "Команды: курс доллара /usd, евро /eur, фунта /gbp. Помощь /help, inline /rates")
        elif command == '/help':
            bot.sendMessage(chat_id, "Связь с разработчиком @nikdmi")



def first(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    r = requests.get(url).json()
    f = (r["Valute"]["USD"]["Value"])
    bot.answerCallbackQuery(query_id, f)


MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': first}).run_as_thread()
print('Alive ...')

while 1:
    time.sleep(10)
