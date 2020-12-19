import bs4
import csv
import requests
from datetime import datetime as dt
import os


def request_gold_price(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    price = float(soup.find('span',{'class':'price-section__current-value'}).string)
    return price

def write_to_file(price):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    file_content = [price, time]
    exist = os.path.exists('gold_price.csv')
    f = open('gold_price.csv', 'a')
    reader = csv.writer(f)
    if not exist:
        header = ('Price', 'Time')
        reader.writerow(header)
    reader.writerow(file_content)
    f.close()



def main():
    URL = 'https://markets.businessinsider.com/commodities/gold-price'
    gold_price = request_gold_price(URL)
    write_to_file(gold_price)

if __name__ == '__main__':
    main()
