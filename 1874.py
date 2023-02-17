'''
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
'''

import sys
from collections import deque
# K 입력
K=int(sys.stdin.readline())

# 크레센도 수열 생성
preparedArray=deque([i for i in range(1,K+1)])


print(preparedArray)

# 입력받은 수열 생성
inputArray=deque()
for x in range(K):
    inputArray.appendleft(int(sys.stdin.readline()))

print(inputArray)

projectArray=deque()
temp=deque()
i=0

# print(inputArray[0])

while(len(preparedArray)!=0):
    if(preparedArray[i]==inputArray[i]):
        projectArray.append(preparedArray.popleft())
        print("+")
        i+=1
    elif(preparedArray[i]<inputArray[i]):
        sub=inputArray[i]-preparedArray[i] #2
        for i in range(sub):
            projectArray.append(preparedArray.popleft())
            print("+")
        for i in range(sub):
            temp.append(projectArray.pop())
            print("-")
        projectArray.append(preparedArray.popleft())
    else:
        pass
        #미완
        

















# # targetArray의 배열을 순회하면서 이것에 맞춰야함

# pointer=preparedArray[-1]

# resultArray=[]
# print(f"pointer=={pointer}")

# for i in targetArray:
#     if pointer< i:
#         for i in range(i-pointer):
#             resultArray.append(preparedArray.pop())












# tempArray=[]
# resultArray=[]
# tempNum=0
# for i in targetArray:
#     print(f"i는 {i}")
#     while(tempNum!=i):
#         tempNum=preparedArray.pop()
#         tempArray.append(tempNum)
#         print(tempArray)
#     resultArray.append(targetArray.pop())

