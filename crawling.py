import requests
from bs4 import BeautifulSoup

res = requests.get('http://store.traders.co.kr/popup/pop_info_off.html')
soup = BeautifulSoup(res.content,'html.parser')
holiday = soup.find("div", id="popwrap",)