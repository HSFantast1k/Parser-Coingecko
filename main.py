import requests
from bs4 import BeautifulSoup


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
responce = requests.get('https://www.coingecko.com/en', headers=HEADERS)
soup = BeautifulSoup(responce.content, 'html.parser')
crypto_name = crypto_cost = []

for cry in soup.find_all('td', class_='py-0 coin-name'): # Парсер названий
    crypto_name.append(cry.get('data-sort'))

for cry_cost in soup.find_all('td', class_='td-price price text-right'):
    crypto_cost.append(cry_cost.find(class_='no-wrap').get_text())

crypto_base = [0] * len(crypto_name)
for i in range(len(crypto_name)):
    crypto_base[i] = [crypto_name[i], crypto_cost[i]]

print(crypto_base)