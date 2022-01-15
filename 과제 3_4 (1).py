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
