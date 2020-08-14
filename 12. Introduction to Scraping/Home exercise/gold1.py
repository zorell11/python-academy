import requests
import os
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup as BS

DATE_FORMAT = '%d.%m.%Y %H:%M'
URL = "https://markets.businessinsider.com/commodities/gold-price"

def request_gold_price():

    r = requests.get(URL)
    soup = BS(r.text, "html.parser")
    price = soup.find('span',{'class':'push-data'}).string

    print('The current price is {}'.format(price))

    price = ''.join([char for char in price if char!=','])

    return price

def write_data(price):

    mode = 'a' if 'gold_price.csv' in os.listdir() else 'w'

    with open('gold_price.csv', mode) as f:
        writer = csv.writer(f)
        writer.writerow([float(price),dt.now().strftime(DATE_FORMAT)])


if __name__=="__main__":
    write_data(request_gold_price())
