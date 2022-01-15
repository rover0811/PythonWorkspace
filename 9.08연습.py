(1+2)*3
(1+2)*3/4

a=5
b=4
print(a+b)
print(a,b)
print(a,b,sep=",") #이런 식으로 구분 가능

for a in range(2,8):print(a,a**2)

value=1234
print(value*2)
print(value/4)

s="서울"
d="부산"
g="대전"
b="대구"
print(s,d,g,b,sep="안녕")
print(s,d,g,b)
a="강아지"
b="고양이"
print(a)
print(b)

print(a,end="귀여워")
print(b)


print(34,56,sep="^^",end="-->") #이경우 개행 안됨
print(78)

age=input("몇 살이세요? ")
print(age)


price=input("가격을 입력하세요: ")
num=input("개수를 입력하세요: ")

sum=int(price)*int(num)
print(type(sum))
print("총액은 %d원입니다" %sum)



price=int(input("가격을 입력하세요: "))
num=int(input("개수를 입력하세요: "))

sum=price*num
print(type(sum))
print("총액은 %d원입니다" %sum)


score=98
score="high"
print(score)

name=input("이름을 입력하세요:")
print("안녕하세요 %s님"%name)

print("%d"%123)
print("%5d"%123)
print("%05d"%123)
