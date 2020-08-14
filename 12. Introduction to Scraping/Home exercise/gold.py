# CTRL + SHIFT + C
import requests
import csv
import os
from bs4 import BeautifulSoup as BS

URL = "https://markets.businessinsider.com/commodities/gold-price"

def get_gold_price(url):
    response = requests.get(url)
    soup = BS(response.text, "html.parser")
    price = soup.find('span',{'class':'push-data'}).string
    price = ''.join(char for char in price if char != ',')
    return price

def print_price(price):
    print('The current price is {}'.format(price))

def write_to_file(price):
    mode = 'a' if 'price.csv' in os.listdir() else 'w'

    with open('price.csv', mode) as f:
        writer = csv.writer(f)
        writer.writerow([float(price)])


def main():
    price = get_gold_price(URL)
    print_price(price)
    write_to_file(price)



if __name__=="__main__":
    main()
    #write_data(request_gold_price())
