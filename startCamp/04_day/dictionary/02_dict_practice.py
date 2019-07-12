"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.

print(sum(score.values())/len(score))





# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
a = sum(scores['a'].values())/len(scores['a'])
b = sum(scores['b'].values())/len(scores['b'])  
print((a+b)/(len(scores)))






# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-100, -5, 2],
    '광주': [0, 0, 0],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
for key, value in city.items():
    average_temp = sum(value) / len(value)
    print(f'{key} : {average_temp}')
# city_1 =sum(city['서울'])/len(city['서울'])
# city_2 =sum(city['대전'])/len(city['대전'])
# city_3 =sum(city['광주'])/len(city['광주'])
# city_4 =sum(city['부산'])/len(city['부산'])
# print(f'서울 : {city_1} \n대전 : {city_2} \n광주 : {city_3} \n부산 : {city_4}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
# max_list =[]
# for key, value in city['서울'].items() :
#     max1 = value
#     if max1 > value :
#     max_list.append[key,value]
#     else max1 <= city :
#     max1 = city
#     print(max_list)


    # if max_item.items()
    #     max_list.append(max_item)
#max1=max(city['서울'])

#print(f'가장 추웠던 곳 : {max1} \n가장 더웠던 곳 : {min1}')
# for key, value, hot in city.items() :
#     hot = city.items.value[0]

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
if city['서울'] == 2 :
    answer = '네, 있습니다.'
else :
    answer = '아니오, 없습니다.'
print(f'{answer}')