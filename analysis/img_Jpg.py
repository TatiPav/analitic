from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://alexbrush.com/nastrojka-postoyannyh-ssylok-s-html-na-kontse.html')
one = BeautifulSoup(html, 'html.parser')

images = one.find_all('img', {'src':re.compile('\.jpg')})

for image in images:
    print(image['src'])