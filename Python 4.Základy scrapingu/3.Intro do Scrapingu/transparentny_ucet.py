import requests,bs4
import csv


def make_soup(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup




def main():
    HEADER = ['Datum', 'Částka', 'Typ', 'Název protiúčtu', 'Zpráva pro příjemce', 'KS', 'VS', 'SS', 'Poznámka']
    URL = "https://ib.fio.cz/ib/transparent?a=2800396030"
    soup = make_soup(URL)
    print(soup)

if __name__ == '__main__':
    main()
