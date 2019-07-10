import requests
import bs4
url = "https://www.bithumb.com/"
selector = '#tableAsset > tbody > tr'
#tableAsset > tbody > tr:nth-child(1) > td:nth-child(1) > p
html = requests.get(url).text
soup = bs4.BeautifulSoup(html,'html.parser')
coins = soup.select(selector)
print(coins)


#print(coiname)
# tr의 리스트[ <btc>, <eth>]

# import csv
# with open('coin.csv') as f:
#     for a in coins:
#         coinname = a.select_one
#         f.write(coinname)