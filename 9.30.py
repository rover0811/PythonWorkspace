num=151
sum=0
while num<=300:
    sum+=num
    num+=2
print("num=",num-2)
print("sum=", sum)

for student in [10, 20,30,40,50]:
    print(student,"번 학생의 성적을 처리한다.")

sum=0
for num in range(1,101):
    sum+=num
print("sum=",sum)

sum=0
for num in range(2,10,2):
    sum+=num
print("sum=",sum)

for x in range(1,51):
    if(x%10==0):
        print("*",end='')
    else:
        print("-",end='')

x=1
while x<=50:
    if (x%10):
        print("-",end="")
    else:
        print("+",end="")
    x+=1

for x in range(1,51):
    if(x%10==5):
        print("+",end='')
    else:
        print("-",end='')

score=[95,85,78,150]
for s in score:
    if (s<0 or s>100):
        break
print("성적처리끝")

for i in range(0,3,1):
    for k in range(0,2,1):
        print("컴퓨터 프로그래밍(i값:%d,k값:%d)"%(i,k))


for dan in range(2,10):
    print(dan,"단")
    for hang in range(2,10):
        print(dan,"*",hang,"=",dan*hang)
    print()

dan=2
while dan<=9:
    hang=2
    print(dan,"단")
    while hang<=9:
        print(dan,"*",hang,"=",dan*hang)
        hang+=1
    dan+=1
    print()

i,hap=0,0
num=0
init_num=int(input("초기값:"))
num=int(input("입력값:"))
for i in range(init_num,num+1,1):
    hap=hap+i
print("1에서 %d까지의 합:%d"%(num,hap))

i,hap=0,0
num=0
init_num=int(input("초기값:"))
close_num=int(input("종료값:"))

for i in range(init_num,close_num+1,1):
    hap=hap+i
print("%d에서 %d까지의 합:%d"%(init_num,close_num,hap))

