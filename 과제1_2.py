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

