# -*- coding: utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get('http://docs.python.jp/2/library/index.html')
soup = BeautifulSoup(r.content,'html.parser')
toctree = soup.find('div', 'toctree-wrapper')
links = toctree.find_all('a')

print(len(links))

for link in links[:3]:
    print(link.text)
