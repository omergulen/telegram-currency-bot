import time
import telepot
import json
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.request import urlopen
from forex_python.converter import CurrencyRates

j = urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10')
j_obj = json.load(j)

c = CurrencyRates()

def btcn_get(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='BTC > USD', callback_data='btcusd')],
        [InlineKeyboardButton(text='BTC > EUR', callback_data='btceur')],
        [InlineKeyboardButton(text='BTC > TRY', callback_data='btctry')],
        [InlineKeyboardButton(text='BTC USD VOLUME 24H', callback_data='btcusdvol')],
        [InlineKeyboardButton(text='BTC EUR VOLUME 24H', callback_data='btceurvol')],
        [InlineKeyboardButton(text='BTC % CHANGE IN 1H ', callback_data='btcperhour')],
    ])
    bot.sendMessage(chat_id, 'BTC ?', reply_markup=keyboard)

def btcn_send(chat_id: object, msg: object, cur: object) -> object:
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if cur == "usd":
        bot.sendMessage(chat_id, "1 BTC = {} USD".format(j_obj[0]["price_usd"]))
    elif cur == "eur":
        bot.sendMessage(chat_id,
                        "1 BTC = {} EUR".format(j_obj[0]["price_eur"]))
    elif cur == "try":
        bot.sendMessage(chat_id,
                        "1 BTC = {} TRY".format(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))))
    elif cur == "buv":
        bot.sendMessage(chat_id,
                        "BTC USD VOLUME IN 24H : {} USD".format(j_obj[0]["24h_volume_usd"]))
    elif cur == "bev":
        bot.sendMessage(chat_id,
                        "BTC EUR VOLUME IN 24H : {} EUR".format(j_obj[0]["volume_eur"]))
    elif cur == "bph":
        bot.sendMessage(chat_id,
                        "BTC % CHANGED IN 1H : {} %".format(j_obj[0]["percent_change_1h"]))

def ltc_get(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='LTC > USD', callback_data='ltcusd')],
        [InlineKeyboardButton(text='LTC > EUR', callback_data='ltceur')],
        [InlineKeyboardButton(text='LTC > TRY', callback_data='ltctry')],
        [InlineKeyboardButton(text='LTC USD VOLUME 24H', callback_data='ltcusdvol')],
        [InlineKeyboardButton(text='LTC EUR VOLUME 24H', callback_data='ltceurvol')],
        [InlineKeyboardButton(text='LTC % CHANGE IN 1H ', callback_data='ltcperhour')],
    ])
    bot.sendMessage(chat_id, 'LTC ?', reply_markup=keyboard)

def ltc_send(chat_id: object, msg: object, cur: object) -> object:
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if cur == "usd":
        bot.sendMessage(chat_id, "1 LTC = {} USD".format(j_obj[3]["price_usd"]))
    elif cur == "eur":
        bot.sendMessage(chat_id,
                        "1 LTC = {} EUR".format(j_obj[3]["price_eur"]))
    elif cur == "try":
        bot.sendMessage(chat_id,
                        "1 LTC = {} TRY".format(c.convert('USD', 'TRY', round(float(j_obj[3]["price_usd"]), 2))))
    elif cur == "buv":
        bot.sendMessage(chat_id,
                        "LTC USD VOLUME IN 24H : {} USD".format(j_obj[3]["24h_volume_usd"]))
    elif cur == "bev":
        bot.sendMessage(chat_id,
                        "LTC EUR VOLUME IN 24H : {} EUR".format(j_obj[3]["volume_eur"]))
    elif cur == "bph":
        bot.sendMessage(chat_id,
                        "LTC % CHANGED IN 1H : {} %".format(j_obj[3]["percent_change_1h"]))

def on_chat_message(msg):
    if msg['text'] == "/btc":
        btcn_get(msg)
    elif msg['text'] == "/ltc":
        ltc_get(msg)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    if query_data == "btcusd":
        btcn_send(from_id, msg, "usd")
    elif query_data == "btceur":
        btcn_send(from_id, msg, "eur")
    elif query_data == "btctry":
        btcn_send(from_id, msg, "try")
    elif query_data == "btcusdvol":
        btcn_send(from_id, msg, "buv")
    elif query_data == "btceurvol":
        btcn_send(from_id,msg, "bev")
    elif query_data == "btcperhour":
        btcn_send(from_id, msg, "bph")

    elif query_data == "ltcusd":
        ltc_send(from_id, msg, "usd")
    elif query_data == "ltceur":
        ltc_send(from_id, msg, "eur")
    elif query_data == "ltctry":
        ltc_send(from_id, msg, "try")
    elif query_data == "ltcusdvol":
        ltc_send(from_id, msg, "buv")
    elif query_data == "ltceurvol":
        ltc_send(from_id,msg, "bev")
    elif query_data == "ltcperhour":
        ltc_send(from_id, msg, "bph")

TOKEN = "*****************************************"

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print('Listening ...')

while 1:
    time.sleep(10)
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10')
    j_obj = json.load(j)
