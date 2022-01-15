# while로 작성해보기

import time
n=1

print("구구단 암기 프로그램")
c= int(input("구구단 몇단을 암기하시겠습니까? "))
print("%d단을 선택하셨습니다." %c)
while n<=9:
    print("%dX%d=%d" %(c,n,c*n)) #양식문자도 분배법칙처럼 묶어서 표현 가능!
    time.sleep(0.01)
    n+=1

print("구구단 암기 프로그램")
c= int(input("구구단 몇단을 암기하시겠습니까? "))
print("%d단을 선택하셨습니다." %c)
for n in range(1,10): # 원래 문법 (시작값, 종료값, 증가값) 그러나 시작 디증가의 디폴트가 1이기에 생략도 가능 그러나 끝 값은 포함안된다
    print("%dX%d=%d" %(c,n,c*n))
    time.sleep(0.01)
    n+=1

a=list(range(30,70,3))
print(sum(a))

n=30
sum=0
while 30<=n<=70:
    if n%3==0:
        sum=sum+n
    n=n+1
print("합계:", sum)