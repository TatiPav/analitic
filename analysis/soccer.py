from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def printText(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        one = BeautifulSoup(html.read(), 'html.parser')
        text = one.h3
    except AttributeError as e:
        return None
    return text

text = printText('https://footbolno.ru/samye-izvestnye-futbolisty-v-mire.html')
if text == None:
    print('Ошибки отсутствия информации')
else:
    print(text)
