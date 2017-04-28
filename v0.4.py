import asyncio
import telepot
import telepot.aio
import json
import re
import logging
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.request import urlopen
from forex_python.converter import CurrencyRates
from datetime import datetime

logging.basicConfig(filename='logs', filemode='a', level=logging.DEBUG, format='%(asctime)s %(message)s')


def comma_me(amount):
    orig = amount
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
    if orig == new:
        return new
    else:
        return comma_me(new)


async def control_currency():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


async def on_chat_message(msg):
    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Chat:', content_type, chat_type, chat_id,
          msg['from']['username'], msg['text'])
    log = 'Chat: ' + content_type + " " + chat_type + " " + str(chat_id) + " " + msg['from']['username'] + " " + msg[
        'text']
    logging.info(log)

    if content_type != 'text':
        return

    if msg['text'] == "/start":
        markup = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text='/BTC'), KeyboardButton(text='/ETH'), KeyboardButton(text='/ETC')],
            [KeyboardButton(text='/XRP'), KeyboardButton(text='/LTC')],
            [KeyboardButton(text='/DASH'), KeyboardButton(text='/XMR')]
        ])
        await bot.sendMessage(chat_id, 'Select currency to get information about.', reply_markup=markup)

    elif msg['text'] == "/BTC":
        control_currency()
        await bot.sendMessage(chat_id, "BitCoin @ {}\n"
                                       "1 BTC = {:.2f} USD\n"
                                       "1 BTC = {:.2f} EUR\n"
                                       "1 BTC = {:.2f} TRY\n"
                                       "BTC-USD Volume in 24h : {} USD\n"
                                       "BTC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(j_obj[0]["price_usd"]),
            float(j_obj[0]["price_eur"]),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/ETC":
        await control_currency()

        await bot.sendMessage(chat_id, "Etherium Classic @ {}\n"
                                       "1 ETC = {:.2f} USD\n"
                                       "1 ETC = {:.2f} EUR\n"
                                       "1 ETC = {:.2f} TRY\n"
                                       "ETC-USD Volume in 24h : {} USD\n"
                                       "ETC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(j_obj[5]["price_usd"]),
            float(j_obj[5]["price_eur"]),
            float(c.convert('USD', 'TRY', round(float(j_obj[5]["price_usd"]), 2))),
            comma_me(j_obj[5]["24h_volume_usd"]),
            comma_me(j_obj[5]["percent_change_24h"])))

    elif msg['text'] == "/XRP":
        await control_currency()

        await bot.sendMessage(chat_id, "Ripple @ {}\n"
                                       "1 XRP = {:.2f} USD\n"
                                       "1 XRP = {:.2f} EUR\n"
                                       "1 XRP = {:.2f} TRY\n"
                                       "XRP-USD Volume in 24h : {} USD\n"
                                       "XRP % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[2]["price_usd"])),
            float(comma_me(j_obj[2]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[2]["price_usd"]), 2))),
            comma_me(j_obj[2]["24h_volume_usd"]),
            comma_me(j_obj[2]["percent_change_24h"])))

    elif msg['text'] == "/ETH":
        await control_currency()

        await bot.sendMessage(chat_id, "Ethereum @ {}\n"
                                       "1 ETH = {:.2f} USD\n"
                                       "1 ETH = {:.2f} EUR\n"
                                       "1 ETH = {:.2f} TRY\n"
                                       "ETH-USD Volume in 24h : {} USD\n"
                                       "ETH % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[1]["price_usd"])),
            float(comma_me(j_obj[1]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[1]["price_usd"]), 2))),
            comma_me(j_obj[1]["24h_volume_usd"]),
            comma_me(j_obj[1]["percent_change_24h"])))

    elif msg['text'] == "/LTC":
        await control_currency()

        await bot.sendMessage(chat_id, "Litecoin @ {}\n"
                                       "1 LTC = {:.2f} USD\n"
                                       "1 LTC = {:.2f} EUR\n"
                                       "1 LTC = {:.2f} TRY\n"
                                       "LTC-USD Volume in 24h : {} USD\n"
                                       "LTC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[3]["price_usd"])),
            float(comma_me(j_obj[3]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[3]["price_usd"]), 2))),
            comma_me(j_obj[3]["24h_volume_usd"]),
            comma_me(j_obj[3]["percent_change_24h"])))

    elif msg['text'] == "/DASH":
        await control_currency()

        await bot.sendMessage(chat_id, "Dash @ {}\n"
                                       "1 DASH = {:.2f} USD\n"
                                       "1 DASH = {:.2f} EUR\n"
                                       "1 DASH = {:.2f} TRY\n"
                                       "DASH-USD Volume in 24h : {} USD\n"
                                       "DASH % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[4]["price_usd"])),
            float(comma_me(j_obj[4]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[4]["price_usd"]), 2))),
            comma_me(j_obj[4]["24h_volume_usd"]),
            comma_me(j_obj[4]["percent_change_24h"])))

    elif msg['text'] == "/XMR":
        await control_currency()

        await bot.sendMessage(chat_id, "Monero @ {}\n"
                                       "1 XMR = {:.2f} USD\n"
                                       "1 XMR = {:.2f} EUR\n"
                                       "1 XMR = {:.2f} TRY\n"
                                       "XMR-USD Volume in 24h : {} USD\n"
                                       "XMR % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[7]["price_usd"])),
            float(comma_me(j_obj[7]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[7]["price_usd"]), 2))),
            comma_me(j_obj[7]["24h_volume_usd"]),
            comma_me(j_obj[7]["percent_change_24h"])))

    elif msg['text'] == "/about":
        await bot.sendMessage(chat_id, "To advice us:\n"
                                       "https://github.com/omergulen/telegram-currency-bot\n"
                                       "or\n"
                                       "omrglen@gmail.com\n"
                                       "Thanks for support!")
        await bot.sendMessage(chat_id, '/start to re-open keyboard')

    else:
        await bot.sendMessage(chat_id, '/start to re-open keyboard\n'
                                       '/about to advice us :))')


TOKEN = "************************************"

bot = telepot.aio.Bot(TOKEN)
answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop({'chat': on_chat_message}))

print('Listening ...')

loop.run_forever()
