score = 80
if score>=90:
    print("장학금 대상자입니다.")
print("수고하셨습니다.")

curHour = int(input("지금 몇시인가요? "))
print("현재시간: %d"%curHour)
preHour=curHour-6
if preHour < 0:
    preHour=preHour+24
print("이전시간: %d"%preHour)

import sys

print("===짝홀 판별 프로그램===")
n= int(input("정수를 입력하세요.: "))

print("정수 %d를 입력했군요"%n)

if n<0:
    print("판별 x")
    print("프로그램 종료")
    sys.exit()

if n % 2 ==0:
    print("당신이 입력한 수는 짝수입니다.")
else:
    print("당신이 입력한 수는 홀수입니다.")

입력년도= int(input("년도 입력: "))
if 입력년도 % 4 ==0:
    print("윤년")
elif 입력년도 % 100==0:
    print("윤년 x")
elif 입력년도 % 400==0:
    print("윤년")
else:
    print("윤년 x")

a = [1,2,3,4,5]
for item in a:
    print(item)

# 과제 1
print("=== 센티미터-> 인치 변환 프로그램 ===")
센터미터길이 = float(input("센터미터 입력: "))
인치길이=센터미터길이/2.54
print( 센터미터길이, "cm는",인치길이, "inch입니다.")

# 과제 2
name= input("이름이 뭐에요? ")
age= float(input("몇 살이에요? "))
height= float(input("키가 몇이에요? "))
print("\n이름: %s"%name)
print("나이: %d살"%age)
print("키: %.2f cm" %height)

# 과제 3
print("=== 원리금 계산 프로그램 ===")
원금= int(input('저축금액 입력: '))
이자=원금*0.0375
세금=이자*0.15
최종=원금+이자-세금
print('원금: %d원'%원금)
print('이자:  %d원'%이자)
print('세금:   
x%d원'%세금)
print('최종: %d원'%최종)


# 과제 4
정수=int(input("정수입력 --> "))
print("10진수:", 정수)

n8=oct(정수)
n8=n8.replace("0o","")
print("08진수:",n8)

n10=hex(정수)
n10=n10.replace("0x","")
print("16진수:",n10)
