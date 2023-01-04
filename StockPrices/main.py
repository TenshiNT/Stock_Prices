from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import textract

# Twilio
SID = 'Your sid'
Auth_Token = 'your token'
cl = Client(SID, Auth_Token)

# Crypto
data_btc = yf.download(
    tickers='BTC-USD', period='10m', interval='15m')
info_raw = str(data_btc).split()
price = float(info_raw[11])

data_eth = yf.download(
    tickers='ETH-USD', period='10m', interval='15m')
info_raw = str(data_eth).split()
price1 = float(info_raw[11])


final_price = round(price, 2)
final_price1 = round(price1, 2)

# Stocks
stock_list = ['AAPL', 'TSLA', 'AMZN', 'COKE',
              'GC=F']
stock_names = ['APPLE', 'TESLA', 'AMZN', 'COKE', 'GOLD']
list_index = 0


def stock_price(symbol: str = 'AAPL') -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "D(ib) Va(m) Maw(65%) Ov(h)"
    return soup.find("div", class_=class_).find("fin-streamer").text


open('message.txt', 'w').close()

with open('message.txt', 'a') as f:
    f.write(
        f'                          Current stock price of {stock_names[0]} is ')
    f.write(f'{stock_price(stock_list[0])}')
    f.write(
        f'                                       Current stock price of {stock_names[1]} is ')
    f.write(f'{stock_price(stock_list[1])}')
    f.write(
        f'                                       Current stock price of {stock_names[2]} is ')
    f.write(f'{stock_price(stock_list[2])}')
    f.write(
        f'                                       Current stock price of {stock_names[3]} is ')
    f.write(f'{stock_price(stock_list[3])}')
    f.write(
        f'                                       Current stock price of {stock_names[4]} is ')
    f.write(f'{stock_price(stock_list[4])}')
    f.write('                                                                                                                     Current price of BITCOIN is ' + str(final_price))
    f.write('                                       Current price of ETHERUM is ' + str(final_price1))

body = textract.process(
    r'C:\Users\Jolec\Desktop\StockPrices\message.txt', encoding='utf-8')

cl.messages.create(
    body=str(body).replace("Sent from your twilio trial account -b'", ""),
    from_='your twilio number',
    to='your phone number')
