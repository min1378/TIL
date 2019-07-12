lunch1 = {
        '중국집' : '02'
} #방법1
print(lunch1)
#방법2
lunch2 = dict(중국집='02')
print(lunch2)

#딕셔너리 내용 추가하기
lunch1['중국집'] # 02 밸류값이 나옴
lunch1['분식집'] = '031' #분식집이라는 키 값과 '031'이라는 밸류값 추가됨!!

#딕셔너리 내용 가져오기

idol = {
    'bts' : {
        '지민' : 24,
        'RM' : 25
    }
}

#랩몬스터의 나이는?

print(idol['bts']['RM'])

print('========================') # 구분선
#딕셔너리 반복문 활용하기

#기본 활용
for key in lunch1 :
    print(key, lunch1[key])

#value만 가져오기

for value in lunch1.values() : 
    print(value)

#key만 가져오기

for key in lunch1.keys() : 
    print(key)

#. items() => key value 가져오기

for key, value in lunch1.items() : 
    print(lunch1.items())
    print(key, value)

# 
sum([1, 3, 4]) #8
len([1, 3, 4]) #3
max([1, 3, 4]) #4
min([1, 3, 4]) #1