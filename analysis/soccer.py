from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://footbolnonnnnnnn.ru/samye-izvestnye-futbolisty-v-mire.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)

else:
    print(html.read())

