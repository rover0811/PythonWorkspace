#1번
from pickletools import string1
from random import randint
while(True):
    comNum=randint(1,6)
    print("컴퓨터의 숫자를 맞춰보세요!")
    try:
        playerNum=int(input())
        if 1<=playerNum and playerNum<=6:
            print("컴퓨터의 숫자는 ",comNum)
            print("플레이어의 숫자는 ",playerNum)
            if(playerNum==comNum):
                print("맞췄어요! 플레이어가 이겼어요!")
            else:
                print("틀렸어요..컴퓨터가 이겼어요")
    except ValueError:
        print("잘못된 입력이에요. 게임을 종료합니다")
        break

# #2번
print("주문 체크 시스템>> 호수를 입력해주세요")
floorNum=int(input())
onlyfloor=floorNum//100
if(onlyfloor <=5):
    print("음식값은 4000원")
elif(5<onlyfloor and onlyfloor<=10):
    print("음식값은 4400원")
elif(10<onlyfloor and onlyfloor<=15):
    print("음식값은 4800원")
elif(15<onlyfloor and onlyfloor<=20):
    print("음식값은 5200원")
elif(20<onlyfloor):
    print("너무 높아서 배달할 수가 없어서 주문이 불가능합니다")

#3번
print("원하는 수를 입력하세요")
sequenceNum=int(input())
sequenceArray=[]
sequenceSum=0
for i in range(sequenceNum+1):
    sequenceArray.append(i)
    sequenceSum+=i
print("수열의 합은",sequenceSum)

#4번
print("문자열을 입력해주세요")
sequencailString=input()
sequencailChecker=0

for j in range(len(sequencailString)):
    if(j==0):
        sequencailChecker+=1
        continue
    elif(sequencailString[j-1]==sequencailString[j]):
        sequencailChecker+=1
    elif(sequencailString[j-1]!=sequencailString[j]):
        print(sequencailString[j-1]+str(sequencailChecker),end='')
        sequencailChecker=1
    if(j==len(sequencailString)-1):
        print(sequencailString[j-1]+str(sequencailChecker),end='')



        








