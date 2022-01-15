import time
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

d=[]
while True :
    d.append(input("좋아하는 과일은 무엇인가요? "))
    if d.count("0")>=1:
        print("프로그램을 종료합니다.")
        break
        
    print(d)


