import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime

url = 'https://stat.molit.go.kr/portal/cate/statMetaView.do?hRsId=58'

response = requests.get(url)

html = response.text
bs = BeautifulSoup(html, "html.parser")

print(bs)

