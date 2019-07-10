from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route('/')                 # endpoint 루트 예를들어, www.google.com/search 이런느낌            
                                #@는 데코레이터 개념이 복잡하다. 지금 설명하기 어렵지만.....       
def hello():                    #함수이름은 다른 함수와 겹치지 않도록 한다.
    #return 'Hello 성민!' 
    return render_template('index.html')# template 폴더를 확인해서 index.html 파일 존재여부 확인 


@app.route('/ssafy')            #무조건 /시작으로해야 인식가능!!
def ssafy():
    return 'Hello SSAFY'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2020, 2, 25)
    td = b_day - today
    return f'{td.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>asdasdasdsad </h1>'


@app.route('/html_lines')
def html_lines():
    return '''
    <h1> 여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''
# @app.route('/greeting/IU')
# def greeting_IU():
#     return '반갑습니다 IU님!'

# @app.route('/greeting/ziont')
# def greeting_ziont():
#     return '반갑습니다 ziont님!'
#                                 #동적으로 받아서 할순없을까?!

@app.route('/greeting/<name>')  #동적으로 name으로 받아서 사용!
def greeting(name):
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return render_template('cube.html', html_num=num, html_result=result)

# 실습

@app.route('/lunch/<int:people>')
def lunch(people):
    #사람 수 만큼의 랜덤 아이템을 menu list에서 
    #뽑아서 보여주는 페이지!
    menu = ['짜장면','유니짜장','탕수육','깐풍기','볶음밥','짬뽕','양장피','유산슬']
    a = random.sample(menu,people)
    return f'추천메뉴는 {a}입니다!'



@app.route('/movie')
def movie():
    movies = ['덩케르크','기생충','토이스토리4','알라딘']
    return render_template('movie.html', movies=movies)

if __name__ == '__main__' :     # 파이썬 실행방법에는 두가지... 1. python @@.py 2. 모듈을 호출하는 방법 import시키면 자동 실행 파이썬은 그 자체로 모듈이 된다.   
                                #__name__이라는 변수는 모든 파이썬에 존재. 모듈 호출로 실행하면 __name__에 __main__이 없다. 해당모듈의 이름이 나옴.
                                # 그러나 @@.py로 실행하면 __name__에 __main__이라는 값이 들어간다. 구분하기 위한 용도
    app.run(debug=True)