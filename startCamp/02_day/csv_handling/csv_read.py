# 1. split
with open('dinner.csv', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines :
        print(line.strip().split(','))  # , 기준으로 문자열을 분리하여 저장 #개행문자가 포함되어서 나온다. strip() 으로 개행문자 삭제~

# 2. csv reader 사용

import csv

with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)