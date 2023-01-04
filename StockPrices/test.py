from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go


def stock_price(symbol: str = 'AAPL') -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "D(ib) Va(m) Maw(65%) Ov(h)"
    return soup.find("div", class_=class_).find("fin-streamer").text


stock_list = ['AAPL', 'TSLA', 'AMZN', 'COKE',
              'GC=F']
stock_names = ['APPLE', 'TESLA', 'AMAZON', 'COKE', 'GOLD']

print(
    f"Current stock price of {stock_names[0]} is {stock_price(stock_list[0])} \n")
print(
    f"Current stock price of {stock_names[1]} is {stock_price(stock_list[1])} \n")
print(
    f"Current stock price of {stock_names[2]} is {stock_price(stock_list[2])} \n")
print(
    f"Current stock price of {stock_names[3]} is {stock_price(stock_list[3])} \n")
print(
    f"Current stock price of {stock_names[4]} is {stock_price(stock_list[4])} \n")
