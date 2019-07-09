# heading

```python
import requests #요청
import bs4 #이쁘게 파싱
url = 'https://www.naver.com'
selector = '.ah_k'

html=requests.get(url).text

soup =bs4.BeautifulSoup(html,'html.parser')
ranks=soup.select(selector)
for ranks in ranks:
    print(ranks.text)

```

![아이유](https://cdnimg.melon.co.kr/cm/artistcrop/images/002/61/143/261143_500.jpg?32b7688ac5eb168fa11891d572f7b23d/melon/resize/416/quality/80/optimize)

| 헤더 | 헤더 | 헤더 |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

*  list

1. number list

[TOC]

TOC[] 목차를 만들어줌

{네이버}{http://www.naver.com}

