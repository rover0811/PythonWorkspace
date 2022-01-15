# print(a)
# print(s)
# print(f)
# print(e)
# print(d)
# print(c)

# a=(1+2)*3
# b=c*d+e
# print(a)
# print(b)
# a=5/2
# b=5//2
# print(a)
# print(b)

a=7%2
b=8%3
c=9%3

print(a)
print(b)
print(c)

a=5
a=a+1
a+=1
print(a)

s1="대한민국"
s2="만세"
print(s1+s2)
print("좋아"*5)

print(20+float("22.5"))

print(float(2.54))
print(round(2.54))
print(round(2.54,1))
print(round(123556,-2))

age=int(input("연령은 어떻게 됩니까?"))
if age<19:
    print("미성년입니다.")

a=3
if a==3:
    print("3이다.")
if a>5:
    print("5보다 크다.")
if a<5:
    print("5보다 작다.")

country=input("what is your country?")
country="Korea"
if country=="Korea":
    print("한국입니다.")
if country=="korea":
    print("한국입니다.")

if ("k">"j"): #k 아스키코드
    print("k")
if ("k"<"j"):
    print("j")

energy=1 #불린 논리값
if energy:
    print("열심히 공부한다.")

a=3
a=int(input("구매횟수는 어떻게 됩니까?"))

if a>11 and a<20:
    print("우수고객")

age=16
if age<19:
    print("study hard")
print("should study hard")

age=22
if age<19:
    print("study hard")
else:
    print("should study hard")

age=20
if age<19:
    print("study hard")
    print("should study hard")
else:
    print("study hard")
    print("will be a good person")

age = int(input("연령"))
 
if age<19:
    print("미성년")
elif 19<=age< 25:
    print("성년")
else:
    print("청장년")

grades= 85
if grades>=90:
    print("a")
elif 80<grades<=90:
    print("b")
elif 70<grades<=80:
    print("c")
elif 60<grades<=70:
    print("d")
else:
    print("f")

man=True
age=22
if man==1:
    if age>=19:
        print("성인 남자")

man=True
age=22
if man==1:
    if age>=19:
        print("성인 남자")
    else:
        print("소년")

a=200

if a<100:
    print("100보다 작다")
    print("거짓이므로 이 문장은 안보임")
print("fin")

if a<100:
    print("100보다 작다")
print("거짓이므로 이 문장은 안보임")
print("fin")

if a<100:
    print("less than 100")

else:
    print("larger than 100")
    print("거짓이므로 이 문장은 안보임")

a=int(input("정수 입력"))

if a%6==0:
    print("5배수")
else:
    print("5배수가 아님")

a=33

if a>50:
    if a<100:
        print("50<x<100")
    else:
        print("larger than 100")
else:
    print("less than 50")

score=int(input())
if score>90:
    print("a")
else:
    if 80<score<=90:
        print("b")
    else:
        if 70<grades<=80: 
            print("c")
        else:
            if 60<grades<=70:
                print("d")
            else:
                print("f")
print("학점입니다.")

grades=int(input())


if grades>=90:
    print("a")
elif 80<grades<=90:
    print("b")
elif 70<grades<=80:
    print("c")
elif 60<grades<=70:
    print("d")
else:
    print("f")


a=int(input("첫번째 수를 입력"))
math=input("계산할 연산자를 입력")
b=int(input("두번째 수를 입력"))

if math=="+":
    print("%d + %d = %d입니다." %(a,b,a+b))
elif math=="-":
    print("%d - %d = %d입니다." %(a,b,a-b))
elif math=="*":
    print("%d * %d = %d입니다." %(a,b,a*b))
elif math=="/":
    print("%d / %d = %d입니다." %(a,b,a/b))
elif math=="%":
    print("%d %% %d = %d입니다." %(a,b,a%b))
elif math=="//":
    print("%d // %d = %d입니다." %(a,b,a//b))
elif math=="**":
    print("%d ** %d = %d입니다." %(a,b,a**b))
else:
    print("알수 없는 연산자.")

student=1

while student<=5:
    print("%d번 학생 성적 처리"%student)
    student+=1

for i in range(0,3,1):
    print(i,"hi doing repeat")

for i in range(0.1,5):
    print(i,"hi doing repeat")
for i in range(0,3,1):
    print("%d: hi doing repeat"%i)
for i in range(100,-1,-5):
    print("%d: hi doing repeat"%i)
