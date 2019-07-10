import requests
import bs4
import csv
# 1. Bithumb 페이지를 가지고 온다.

url='https://www.bithumb.com/'
response = requests.get(url)
#print(reponse) #응답 확인
html = response.text # 응답받은 객체에서 html 문서를 string으로 가지고 옴
# print(html) # html형식이 아닌 일반 문자열로 저장되어있음을 확인

#2. Beautiful Soup 모듈을 이용하여 string type의 html을 파싱한다!

soup = bs4.BeautifulSoup(html, 'html.parser')
#print(type(soup)) # bs4.BeautifulSoup 형식으로 변환

#.3 각 코인의 정보가 담겨있는 table row데이터를 list 형태로 가져온다.

# 테이블 row는 너무 많으니 coin_list는 리스트로 가져온다.
coins = soup.select('.coin_list tr') #띄어쓰기로 접근 : 모든 하위 차일드중에 tr이 있다면 다가져와라 >는 바로 앞에 있는것만 추출
#print(coins) #coins 들어왔는지 확인 

#5. csv파일 작성 csw writer를 이용해서...

with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f :
    csv_writer =csv.writer(f)

        #4. 각 코인을 순회하며 필요한 정보만 추출한다.

    for coin in coins:
        #각 코인의 이름과 시세 데이터를 추출
        coin_name =  coin.select_one('td:nth-child(1) > p > a > strong').text.strip().replace('NEW','')
        coin_price = coin.select_one('td:nth-child(2) > strong').text.replace(',','').replace('원','')
        data = (coin_name, coin_price)
        print(data)
        csv_writer.writerow(data) #csv_wrtier.writerow는 튜플로 입력된다.
    
        #print(coin_name) # coin_name 확인