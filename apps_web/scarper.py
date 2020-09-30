import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/Sony-Frame-Interchangeable-Camera-SEL2870/dp/B00Q2KEVA2/ref=sr_1_1_sspa?dchild=1&keywords=sony+a7&qid=1599675689&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOEM1SExLMFU0SVlKJmVuY3J5cHRlZElkPUEwMzQxODgyM1VNVDc3VVJVVkY1USZlbmNyeXB0ZWRBZElkPUEwMTI3ODk3MzBXTVg0ODRVNEUyNiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

#URL = "http://dataquestio.github.io/web-scraping-pages/simple.html"
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

#print(soup.prettify())
title =soup.findAll('span')
print(title)
