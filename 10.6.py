s='python'
print(s[2])
print(s[-2])

for c in s:
    print(c,end=" ")

print(s[2:5])#[a:b]=a~b-1
print(s[3:])
print(s[:4])
print(s[2:-2])

file="20171224-104830.jpg"
print("촬영날짜 :"+file[4:6]+"월"+file[6:8]+"일")
print("촬영시간 :"+file[9:11]+"시"+file[11:13]+"분")
print("확장자 :"+file[-3:])

y="월화수목금토일"
print(y[::2])#[시작점:종료점:단계(음수면 역순 양수면 정순, 2이면 2탕씩 건너뛴다는 의미)]
print(y[::-1])

s="python programming"
print(len(s))#문자열 길이
print(s.find('o'))#첫번째 o의 위치
print(s.rfind("o"))#뒤에서부터 찾는 o의 위치
print(s.index("r"))#find와 동일 그러나 값이 없을 때 find는 -1을 리턴, index는 에러를 냄
print(s.count("n"))#갯수

s='''생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 생각하지 않으려고 하는 생각이 옳은 생각이라고 생각합니다.'''
print("생각 횟수:",s.count("생각"))

s="python programming"
print("a" in s)
print("z" in s)
print("pro" in s)
print("x" not in s)

name="김한결"
if name.startswith("김"):
    print("김가입니다.")
if name.startswith("한"):
    print("한가입니다.")

file="girl.jpg"
if file.endswith(".jpg"):
    print("그림 파일입니다.")

height=input("키를 입력하세요")
if height.isdecimal():
    print("키=",height)
else:
    print("숫자만 입력하시오")

s="Good morning. my love KIM"

print(s.lower())# 다 소문자로
print(s.upper())# 다 대문자로
print(s)

print(s.swapcase())# 소->대 대->소
print(s.capitalize())# 맨 처음만 대문자화. 나머지 소문자화
print(s.title())#각각의 시작을 대문자화

python=input("파이썬의 영문 철자를 입력하시오. :")
if python.lower()=="python":
    print("right!")

s= "   angel   "
print(s+"님")
print(s.lstrip()+"님") #좌 공백 제거
print(s.rstrip()+"님") #우 공백 제거
print(s.strip()+"님") #좌우공백 제거

s="짜장 짬뽕 탕슉"
print(s.split())

s2="서울->대전->대구->부산"
city=s2.split("->")
print(city)
for c in city:
    print(c,"찍고",end=" ")

traveler="""강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도삼백리\n\n술 익는 마을마다\n타는 저녁놀\n구름에 달 가듯이\n가는 나그네"""
poet=traveler.splitlines()
for line in poet:
    print(line)

s="._."
print(s.join("대한민국"))

s2="서울->대전->대구->부산"
city=s2.split("->")
print("찍고".join(city))

s="독도는 일본땅이다. 대마도도 일본땅이다."
print(s)
print(s.replace("일본","한국"))

message="안녕하세요."
print(message.ljust(30))#좌
print(message.rjust(30))#우
print(message.center(30))#중

traveler="""강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도삼백리\n\n술 익는 마을마다\n타는 저녁놀\n구름에 달 가듯이\n가는 나그네"""
poet=traveler.splitlines()
for line in poet:
    print(line.center(30))

price=500
print("궁금하면"+str(price)+"원!")

price=500
print("궁금하면 %d원!" %price)

month=8
day=15
anni="광복절"

print("%d월%d일은 %s이다."%(month,day,anni))

value=123
print("###%d###" %value)
print("###%5d###" %value)
print("###%10d###" %value)
print("###%1d###" %value)

price=[30,13500,2000]

for p in price:
    print("가격: %d원"%p)
for p in price:
    print("가격: %7d원"%p)

price=[30,13500,2000]

for p in price:
    print("가격: %-7d원"%p)#7자리 만들어 좌정렬

pie=3.14159265
print("%10f"%pie)
print("%10.8f"%pie)
print("%10.5f"%pie)
print("%10.2f"%pie)

name="한결"
age=16
height=162.5
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name,age,height)) #{순서:형식}

print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name,age,height))

score=[88,95,70,100,99]

sum=0

for s in score:
    sum+=s
print("총점: %d"%sum )
print("평균: ",sum/len(score) )

nums=[0,1,2,3,4,5,6,7,8,9]

print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

score=[88,95,70,100,90]

print(score[2])
score[2]=55
print(score[2])
print(score)

nums=[0,1,2,3,4,5,6,7,8,9]
nums[2:5]=[20,30,40]
print(nums)
nums[6:8]=[90,91,92,93,94]#??
print(nums)

nums=[0,1,2,3,4,5,6,7,8,9]
nums[2:5]=[]
print(nums)
del nums[4]
print(nums)

list1=[1,2,3,4,5]
list2=[10,11]
listadd=list1+list2
print(listadd)
listmulti=list2*3
print(listmulti)

lol=[[1,2,3],[4,5],[6,7,8,9,]]
print(lol[0])

print(lol[2][1])#3번째 리스트의 2번째 항

for sub in lol:
    for item in sub:
        print(item,end=" ")
    print()



score=[
    [88,76,92,98],
    [65,70,58,82],
    [82,80,78,88]
    ]
total=0
totalsub=0
for student in score:
    sum=0
    for subject in student:
        sum+=subject
    subjects=len(student)
    print("총점 %d, 평균 %.2f"%(sum,sum/subjects))
    total += sum
    totalsub+= subjects
print("전체평균 %.2f"%(total/totalsub))

nums=[n*2 for n in range(1,11)]
for i in nums:
    print(i, end=", ")

nums=[1,2,3,4]
nums.append(5)
print(nums)
nums.insert(2,99)#(위치, 넣을 것)
print(nums)

nums=[1,2,3,4]
nums[2:2]=[90,91,92]
print(nums)

nums=[1,2,3,4]
nums[2]=[90,91,92]
print(nums)





