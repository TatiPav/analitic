from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://footbolno.ru/samye-izvestnye-futbolisty-v-mire.html")
except HTTPError as e:
    print(e)
else:
    one = BeautifulSoup(html.read(), 'html.parser')
    # print(html.read())
    print(one.h2)
