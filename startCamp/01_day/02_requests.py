import requests # requests를 사용하기 위한 
import bs4 #BeautifulSoup를 사용하기 위한 서드파티// 스트링을 보기 편하게 객체로 만들어주는 함수

url = 'https://finance.naver.com/sise/' #요청받을 url

response = requests.get(url) #response.txt 
html =response.text #응답받은 모든 html을 text로 변환
print(response)
print(response.status_code)
soup = bs4.BeautifulSoup(html,'html.parser') #parser 접근할 수 있는 객체로 만들어주는 과정
kospi = soup.select_one('#KOSPI_now').text #parsing을 했기 때문에 이렇게 접근할 수 있다. id는 #을 붙여준다.
print(kospi)


