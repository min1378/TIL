import requests #요청
import bs4 #이쁘게 파싱
url = 'https://www.naver.com'
selector = '.ah_k'

html=requests.get(url).text

soup =bs4.BeautifulSoup(html,'html.parser')
ranks=soup.select(selector)
for ranks in ranks:
    print(ranks.text)
