# import time
# s1="김현수"
# s2="예뻐!->귀여워!->섹시해!->완벽해"

# h=s2.split("->")

# for c in h:
#     print("김현수",c,end=" ")

    #     
    #012345
import time

str="aaa"
speed=1
k=0
for i in range(0,len(str)-1,1):
    for k in range(0-speed,len(str)-speed,1):
        print(str[k],end='')
        k+=1
        time.sleep(0.5)
    speed+=1
    print()



#연세 문자 넣기
text='yonsei'
speed=2
# 여기서부터 코드 작성

originaltext=text
while string != text :
    line = []
    for k in range(len(string)):
        if k + speed <= len(string)-1 :
           line.append(string[k+speed])
        else :
           line.append(string[k+speed-len(string)])
    string = "".join(line)
    print(string)
    if string == text :
       break





