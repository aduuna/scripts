from requests import get
from bs4 import BeautifulSoup

page = get('https://tonaton.com/en/ads/ghana/electronics')
html = BeautifulSoup(page,'html.parser')
items = html.select('ui-item')

for item in items:
    price=item.select('.items-info')[0].text
    name=item.select('.items-title')[0].text
    print(price)

