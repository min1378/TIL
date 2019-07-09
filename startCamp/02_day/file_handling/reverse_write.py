#ssafy.txt 파일을 읽어서
# 역순으로 revesed_ssafy.txt 파일로 저장
with open('ssafy.txt', 'r') as f :
    lines=f.readlines() # list의 형식으로 각 라인을 item 삼아 반환하기 때문....
   # print(lines)
lines.reverse() # list를 반대로 뒤집는다. 
print(lines)
with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)

