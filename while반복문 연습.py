n=1
import time

while n<=5 :
    print("파이썬 재밌네!-->", n)
    time.sleep(1)
    n=n+1
print("종료합니다.",n)

while n<=10:
    
    print(n)
    n+=1
    time.sleep(0.5)
print("숫자세기 끝!")  
  
n=10
while n<=100:
    print(n)
    n=n+10
    time.sleep(0.2)
print("숫자세기 완료했습니다.")

n=100
while n<=150:
    print(n)
    n=n+5
    time.sleep(0.2)
print("숫자세기 완료습니다.")

import time

n=1

print("===구구단 암기 프로그램===")
cn=int(input("구구단 몇 단을 암기하시겠습니까? "))

if 2<= cn <=9:
    print("구구단 %d단을 선택하셨습니다." %cn)
    while n<=9:

        cal=n*cn
        print("%dx" %cn,n,"=",cal) 
        n=n+1
        time.sleep(0.01)
    print("구구단 %d단이 모두 출력되었습니다." %cn)

else:
    print("2~9 사이의 정수만 입력 가능합니다.")

import time

print("===구구단 암기 프로그램===")
cn=int(input("구구단 몇 단을 암기하시겠습니까? "))

if 2<= cn <=9:
    print("구구단 %d단을 선택하셨습니다." %cn)
    for n in range(1,10):
        cal=n*cn
        print("%d X"%cn,n,"=",cal)
        n=n+1
        time.sleep(0.5)
else:
    print("2~9 사이의 정수만 입력 가능합니다.")
    
a=list(range(30,70,3))
print(sum(a))

n=30
sum=0
while 30<=n<=70:
    if n%3==0:
        sum=sum+n
    n=n+1
print("합계:", sum)
    

    



