#!/usr/bin/env python
#-*-coding:utf-8-*-


import asyncio
import logging
import re
import requests
import telepot
import telepot.aio
from datetime import datetime


logging.basicConfig(
    filename='logs',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
    )


API_URL = 'https://api.coinmarketcap.com/v1/ticker'


def comma_me(amount):
    orig = amount
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
    if orig == new:
        return new
    else:
        return comma_me(new)


def get_from_api(url=API_URL, convert='TRY', limit=None):
    """Getting infos from API using requests"""
    params = {'convert': convert}
    if limit:
        params['limit'] = limit
    response = requests.get(url, params=params)
    if response.status_code != 200:
        error_msg = "Couldn't get infos from API"
        raise ConnectionError(error_msg)
    else:
        result = response.json()
        return result


class Currency(object):
    """Representation of a currency in CoinMarketCap API"""

    def __init__(self, symbol, id=None):
        self.symbol = symbol.upper()

    def __repr__(self):
        return '<Currency {}>'.format(self.symbol)

    @staticmethod
    def all():
        """Returns a dict where keys are currencies' symbols
           and values are names"""
        result = get_from_api(API_URL)
        response = []
        for infos in result:
            currency = Currency(infos['symbol'], infos['id'])
            for key, value in infos.items():
                if key not in ['symbol']:
                    setattr(currency, key, value)
            response.append(currency)
        return response


async def on_chat_message(msg):
    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    text = msg['text'].upper()

    try:
        username = msg['from']['username']
        log = ('Chat: {content_type} '
               '{chat_type} {chat_id} '
               '{username} {text}').format(
            content_type=content_type,
            chat_type=chat_type,
            chat_id=chat_id,
            username=username,
            text=text
        )
    except:
        log = ('Chat: {content_type} '
               '{chat_type} {chat_id} '
               '{username} {text}').format(
            content_type=content_type,
            chat_type=chat_type,
            chat_id=chat_id,
            username="no username",
            text=text
        )

    print(date, log)
    logging.info(log)

    CURRENCIES = {
        currency.symbol: currency
        for currency in Currency.all()
    }

    if content_type != 'text':
        return

    if text == '/START':
        await bot.sendMessage(chat_id,"Type currency name.\n")

    elif text == '/ABOUT' or text == '/ABOUT@CCRYPTBOT':
        advice_msg = ('To advice us:\n'
                      'https://github.com/omergulen/telegram-currency-bot\n'
                      'or\n'
                      'omrglen@gmail.com\n'
                      'Thanks for support!')
        await bot.sendMessage(chat_id, advice_msg)
        await bot.sendMessage(chat_id, 'Type a currency name to get information about it.')

    command, text = text.split()

    if command == "/P" and text in CURRENCIES:
        currency = CURRENCIES[text[:]]

        a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b = currency.percent_change_24h


        if float(b) >= 20:
            b = " 🚀"
        elif float(b) > 0:
            b = " 🔺"
        elif float(b) < 0:
            b = " 🔻"
        else:
            b = ""
            
        if currency.symbol != 'BTC':
            response = ('{name} : {date}\n'
                        '= {price_btc:.8f} BTC\n'
                        '= {price_usd:.2f} USD\n'
                        '= {price_try:.2f} TRY\n'
                        '{symbol}-USD Vol. 24h: {usd_volume} USD\n'
                        '{symbol} % Change 24h: {percent_change}% ' + b).format(
                            name=currency.name,
                            date=a[:-8] + str(int(a[-8:-6]) + 3) + a[-6:],
                            symbol=currency.symbol,
                            price_btc=float(currency.price_btc),
                            price_usd=float(currency.price_usd),
                            price_try=float(currency.price_try),
                            usd_volume=comma_me(getattr(currency,'24h_volume_usd')),
                            percent_change=currency.percent_change_24h
                            )
        else:
            response = ('{name} : {date}\n'
                        '= {price_usd:.2f} USD\n'
                        '= {price_try:.2f} TRY\n'
                        '{symbol}-USD Vol. 24h: {usd_volume} USD\n'
                        '{symbol} % Change 24h: {percent_change}% ' + b).format(
                name=currency.name,
                date=a[:-8] + str(int(a[-8:-6]) + 3) + a[-6:],
                symbol=currency.symbol,
                price_usd=float(currency.price_usd),
                price_try=float(currency.price_try),
                usd_volume=comma_me(getattr(currency, '24h_volume_usd')),
                percent_change=currency.percent_change_24h
            )
        await bot.sendMessage(chat_id, response)


if __name__ == '__main__':
    TOKEN =  "******************************************"

    CURRENCIES = {
        currency.symbol: currency
        for currency in Currency.all()
        }

    bot = telepot.aio.Bot(TOKEN)
    answerer = telepot.aio.helper.Answerer(bot)

    loop = asyncio.get_event_loop()
    loop.create_task(bot.message_loop({'chat': on_chat_message}))

    print('Listening ...')

    loop.run_forever()
