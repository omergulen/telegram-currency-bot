import asyncio
import telepot
import telepot.aio
import json
import re
import logging
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
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


def control_currency_btc():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_eth():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_ltc():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_xrp():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_etc():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/ethereum-classic/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_xmr():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/monero/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_dash():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/dash/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_bch():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_xem():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/nem/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_bcc():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/bitconnect/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_neo():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/neo/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_iota():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/iota/?convert=EUR')
    global j_obj
    j_obj = json.load(j)

    global c
    c = CurrencyRates()


def control_currency_omg():
    j = urlopen('https://api.coinmarketcap.com/v1/ticker/omisego/?convert=EUR')
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
            [KeyboardButton(text='/DASH'), KeyboardButton(text='/XMR')],
            [KeyboardButton(text='/BCH'), KeyboardButton(text='/XEM')],
            [KeyboardButton(text='/BCC'), KeyboardButton(text='/NEO')],
            [KeyboardButton(text='/IOTA'), KeyboardButton(text='/OMG')]
        ])
        await bot.sendMessage(chat_id, 'Select currency to get information about.', reply_markup=markup)

    elif msg['text'] == "/BTC":
        control_currency_btc()
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
        control_currency_etc()

        await bot.sendMessage(chat_id, "Etherium Classic @ {}\n"
                                       "1 ETC = {:.2f} USD\n"
                                       "1 ETC = {:.2f} EUR\n"
                                       "1 ETC = {:.2f} TRY\n"
                                       "ETC-USD Volume in 24h : {} USD\n"
                                       "ETC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(j_obj[0]["price_usd"]),
            float(j_obj[0]["price_eur"]),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/XRP":
        control_currency_xrp()

        await bot.sendMessage(chat_id, "Ripple @ {}\n"
                                       "1 XRP = {:.2f} USD\n"
                                       "1 XRP = {:.2f} EUR\n"
                                       "1 XRP = {:.2f} TRY\n"
                                       "XRP-USD Volume in 24h : {} USD\n"
                                       "XRP % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/ETH":
        control_currency_eth()

        await bot.sendMessage(chat_id, "Ethereum @ {}\n"
                                       "1 ETH = {:.2f} USD\n"
                                       "1 ETH = {:.2f} EUR\n"
                                       "1 ETH = {:.2f} TRY\n"
                                       "ETH-USD Volume in 24h : {} USD\n"
                                       "ETH % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/LTC":
        control_currency_ltc()

        await bot.sendMessage(chat_id, "Litecoin @ {}\n"
                                       "1 LTC = {:.2f} USD\n"
                                       "1 LTC = {:.2f} EUR\n"
                                       "1 LTC = {:.2f} TRY\n"
                                       "LTC-USD Volume in 24h : {} USD\n"
                                       "LTC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/DASH":
        control_currency_dash()

        await bot.sendMessage(chat_id, "Dash @ {}\n"
                                       "1 DASH = {:.2f} USD\n"
                                       "1 DASH = {:.2f} EUR\n"
                                       "1 DASH = {:.2f} TRY\n"
                                       "DASH-USD Volume in 24h : {} USD\n"
                                       "DASH % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/XMR":
        control_currency_xmr()

        await bot.sendMessage(chat_id, "Monero @ {}\n"
                                       "1 XMR = {:.2f} USD\n"
                                       "1 XMR = {:.2f} EUR\n"
                                       "1 XMR = {:.2f} TRY\n"
                                       "XMR-USD Volume in 24h : {} USD\n"
                                       "XMR % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/BCH":
        control_currency_bch()

        await bot.sendMessage(chat_id, "Bitcoin Cash @ {}\n"
                                       "1 BCH = {:.2f} USD\n"
                                       "1 BCH = {:.2f} EUR\n"
                                       "1 BCH = {:.2f} TRY\n"
                                       "BCH-USD Volume in 24h : {} USD\n"
                                       "BCH % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/XEM":
        control_currency_xem()

        await bot.sendMessage(chat_id, "Nem @ {}\n"
                                       "1 XEM = {:.2f} USD\n"
                                       "1 XEM = {:.2f} EUR\n"
                                       "1 XEM = {:.2f} TRY\n"
                                       "XEM-USD Volume in 24h : {} USD\n"
                                       "XEM % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/BCC":
        control_currency_bcc()

        await bot.sendMessage(chat_id, "BitConnect @ {}\n"
                                       "1 BCC = {:.2f} USD\n"
                                       "1 BCC = {:.2f} EUR\n"
                                       "1 BCC = {:.2f} TRY\n"
                                       "BCC-USD Volume in 24h : {} USD\n"
                                       "BCC % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/NEO":
        control_currency_neo()

        await bot.sendMessage(chat_id, "Neo @ {}\n"
                                       "1 NEO = {:.2f} USD\n"
                                       "1 NEP = {:.2f} EUR\n"
                                       "1 NEO = {:.2f} TRY\n"
                                       "NEO-USD Volume in 24h : {} USD\n"
                                       "NEO % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/IOTA":
        control_currency_iota()

        await bot.sendMessage(chat_id, "Iota @ {}\n"
                                       "1 IOTA = {:.2f} USD\n"
                                       "1 IOTA = {:.2f} EUR\n"
                                       "1 IOTA = {:.2f} TRY\n"
                                       "IOTA-USD Volume in 24h : {} USD\n"
                                       "IOTA % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

    elif msg['text'] == "/OMG":
        control_currency_omg()

        await bot.sendMessage(chat_id, "OmiseGO @ {}\n"
                                       "1 OMG = {:.2f} USD\n"
                                       "1 OMG = {:.2f} EUR\n"
                                       "1 OMG = {:.2f} TRY\n"
                                       "OMG-USD Volume in 24h : {} USD\n"
                                       "OMG % Changed in 24h : {} %".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            float(comma_me(j_obj[0]["price_usd"])),
            float(comma_me(j_obj[0]["price_eur"])),
            float(c.convert('USD', 'TRY', round(float(j_obj[0]["price_usd"]), 2))),
            comma_me(j_obj[0]["24h_volume_usd"]),
            comma_me(j_obj[0]["percent_change_24h"])))

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


TOKEN =  "**************************************"

bot = telepot.aio.Bot(TOKEN)
answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop({'chat': on_chat_message}))

print('Listening ...')

loop.run_forever()
