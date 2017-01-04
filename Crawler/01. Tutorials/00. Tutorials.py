# pip install requests
# pip install bs4 or beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://codesimu.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('h2 > a'):
            href = 'http://codesimu.tistory.com' + link.get('href')
            title = link.string
            print(href)
            print(title)

        f = open("plain_text.txt", 'w')
        f.write(plain_text)
        f.close()
        page += 1   

spider(2)