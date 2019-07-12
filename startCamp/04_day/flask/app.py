from flask import Flask, render_template, request #requests랑 다름 flask 자체 제공 함수 사용자의 요청을 확인할 수 있는 객체
import requests
import bs4
app = Flask(__name__)


@app.route('/')   # / => root 
def index():
    return 'hello world'



@app.route('/greeting/<string:name>') #입력받아올땐 꺽쇠 <> 사용!!!!!
def hello(name):
    #return f'안녕하세요 {name}님'
    return render_template('greeting.html', html_name=name)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age= request.args.get('age')
    return f'Pong! age: {age}'

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')

@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # Message
    #Ascii Art API를 활용하여 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)


@app.route('/lotto_input')
def lotto_input():
    return render_template('lotto_input.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    lotto_number = request.args.get('text').split()
    
    url=f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # Json Type의 파일을 파이썬 dictionary로 parsing해줘!!!!!!
    
    #for key, val in lotto_info.items():
    winner =[]
    for i in range(1,7) :
        winner.append(str(lotto_info[f'drwtNo{i}']))
    #winner.sort()
    print(winner)    
    print(lotto_number)

    #번호 교집합 개수 찾기              
    if len(lotto_number) == 6:          # 사용자가 보낸 숫자가 6개가 맞는지 확인
        matched = 0                     #교집합 개수 초기화
        for number in lotto_number:     #사용자가 보낸 숫자만큼 돌림
            if number in winner:            #사용자가 보낸 숫자와 1등번호를 비교
                matched += 1            #교집합 발생시 1씩 증가
    if matched == 6:
        result = "1등"
    elif matched == 5:
        if str(lotto_info['bnusNo']) in lotto_number:
            result ="2등"
        else :
            result ="3등"
    elif matched == 4:
            result = "4등"
    elif matched == 3:
            result = "5등"
    else:
            result = '꽝'
    
    return render_template('lotto_result.html', result=result)


















if __name__ == '__main__' :     # 파이썬 실행방법에는 두가지... 1. python @@.py 2. 모듈을 호출하는 방법 import시키면 자동 실행 파이썬은 그 자체로 모듈이 된다.   
                                #__name__이라는 변수는 모든 파이썬에 존재. 모듈 호출로 실행하면 __name__에 __main__이 없다. 해당모듈의 이름이 나옴.
                                # 그러나 @@.py로 실행하면 __name__에 __main__이라는 값이 들어간다. 구분하기 위한 용도
    app.run(debug=True)