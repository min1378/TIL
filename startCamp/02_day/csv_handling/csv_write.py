dinner = {
    '양자강' : '02-557-4221', #차돌
    '김밥카페' : '02-553-3181', #라돈
    '순남시래기' : '02-508-0887' #보쌈정식
}
print(dinner.items()) #  둘다 가져오기
print(dinner.keys())  # 키만 가져오기
print(dinner.values()) # 밸류만 가져오기

# 1.String formatting

with open('dinner.csv', 'w', encoding="utf-8") as f:
    #['양자강','02-557-4221']
   for item in dinner.items() :
       f.write(f'{item[0]},{item[1]}\n') # 양자강,02-557-4221

# 2. csv writer 사용하기!
import csv
with open('dinner.csv', 'w', encoding="utf-8", newline='') as f: #newline='' 을 써줘야 줄이 띄어진 상태가 발생하지않는다. 윈도우에서 발생하는 이슈 #옵션으로줄떄는 붙여서 작성
    csv_writer = csv.writer(f) # f 라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
                                    # 빈 한줄 넣어주는게 관습