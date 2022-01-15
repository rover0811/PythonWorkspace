#6주차 과제 1
def f(x):
    y=(3*x**2)+(5*x)+7
    return y

print("함수 호출")
print("f(15)=", f(15))
print("f(20)=", f(20))
print("f(25)=", f(25))
#6주차 과제 2
def d(a,b):
    y= 0.5*a*b
    return y
 
print("삼각형 넓이 계산 프로그램")
a=int(input("삼각형의 밑변은 몇 cm 입니까?" ))
b=int(input("삼각형의 높이은 몇 cm 입니까?" ))
print("삼각형의 넓이는",d(a,b),"cm^2입니다")

#6주차 과제 3
def score(s):
    if s<20:
        return "F"
    elif 20<=s<40:
        return "D"
    elif 40<=s<60:
        return "C"
    elif 60<=s<80:
        return "B"
    elif 80<=s<=100:
        return "A"

print("학점 계산 프로그램")
s= int(input("당신의 점수는 몇점입니까? "))
print("당신의 학점은",score(s),"입니다.")

#6주차 과제 4

def odd(x):
    if x%2==1:
        return "홀수"
    elif x%2==0:
        return "짝수"
print("홀수, 짝수 판별 프로그램")
x=int(input("아무 정수나 입력하시오. "))
print("이 수는",odd(x),"입니다.")

import time

n=1
#과제 1-1

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
#과제 1-2

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

# 과제2

n=30
sum=0
while 30<=n<=70:
    if n%3==0:
        sum=sum+n
    n=n+1
print("합계:", sum)

import time
# 과제3
a=[] #리스트 맥이기전에 항상 빈 리스트 생성!
for i in range(50,100,3):
    a.append(i)
print(a)

b=[]
for t in range(50,101,5):
    b.append(t) #apeend 추가
print(b)

union=list(set(a)|set(b)) #집합 계산은 set로 넘기기, 합집합 연산자는 |
print(union)
print(sum(union))

# 과제 4
d=[]
while True :
    d.append(input("좋아하는 과일은 무엇인가요? "))
    if d.count("0")>=1:
        print("프로그램을 종료합니다.")
        break
        
    print(d)
