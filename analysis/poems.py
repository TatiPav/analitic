from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stihi.ru/rec_author.html')
ps = BeautifulSoup(html, "html.parser")
licenseLot = ps.findAll('div', {'class': 'recstihi'})
for license in licenseLot:
    print(license.get_text())