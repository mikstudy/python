import time
import requests
from bs4 import BeautifulSoup

def spider():
    url = "http://www.naver.com"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')

    ranks = soup.find("div", {"class": "rankup"})

    for keyword in ranks.findAll('li'):
        print(keyword.a['title'])

def funcTimer(count):
    while 0 < count:
        time.sleep(1)
        print(time.strftime("%Y-%m-%d %H:%M", time.localtime()))
        spider()
        print()
        count -= 1

funcTimer(3)
#spider()


