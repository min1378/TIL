f = open('ssafy.txt', 'r')
all_text = f.read() # all text 전체,
#print(all_text)
f.close()

with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    #print(all_text)

with open('with_ssafy.txt', 'r') as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip()) #공백이나 개행을 지워주는 strip()