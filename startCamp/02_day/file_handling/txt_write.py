#열기모드 
# r : 읽기, w: 쓰기(write - 덮어쓰기), a : 추가(append)
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'this is line {i+1} \n') #파일 쓰기 10줄 반복
f.close() # 끝날땐 파일을 항상 꺼줘야한다. 메모리 어디선가 꺼지지 않고 존재한다.

with open('with_ssafy.txt', 'w') as f:  #컨텍스트 매니저 오픈하고 f로 파일이름을 주겠다. with로 오픈했을때는 반환값이 없어 할당해주는 게 불가능하다. 연 파일을 f라 하겠다 라고 한당.
    for i in range(10):
        f.write(f'this is line {i+1}\n') #자동으로 close 되기 때문에 f.close를 해줄 필요가 없다.

with open('ssafy.txt', 'w', encoding='utf-8') as f : 
    f.writelines()                                        