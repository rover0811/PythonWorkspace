'''
    문제: 무게와 값어치가 주어진 n개의 아이템이 있다고 하자. 무게와 값어치는 양의 정수이다.
        게다가 양의 정수 W도 주어진다. 무게의 합이 W가 넘지 못한다는 제약 하에서 총 값어치가 최대가
        되는 아이템의 집합을 구하시오
    입력: 양의 정수 n과 W
          배열 w(무게)와 p(가격),
          인덱스의 범위는 1부터 n까지이고
          각 배열은 p[i]/w[i] 값에 따라서 큰 수부터 차례로 정렬된 정수를 포함한다.
    출력: 배열 bestset
          bestset[i]의 값은 i번째 아이템이 최적의 해에 포함되어 있으면 yes,
          없으면 'no'이다
          최대 값어치를 나타내는 정수 maxprofit
'''
from copy import deepcopy

def promising(i : int, profit : int, weight : int) -> bool:
    global bound, totweight

    
    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit      
        totweight = weight

        while j <= n and totweight + w[j] <= W:

            totweight += w[j]
            bound += p[j]
            j += 1
        
        k = j
        if k <= n:
            bound += (W - totweight) * (p[k] // w[k])

        return bound > maxprofit


def func(i : int, profit : int, weight : int) -> None:
    global maxprofit, bestset,numbest
    if weight <= W and profit >= maxprofit:
        maxprofit = profit
        bestset = deepcopy(include)
        numbest=i

    flag = promising(i, profit, weight)  
    print(i, weight, profit, bound, maxprofit) #트리 출력 부분
    #print(f"{i},weight: {weight},profit: {profit},bound: {bound},maxprofit:{maxprofit}")

    if flag:
        
        include[i + 1] = True
        func(i + 1, profit + p[i + 1], weight + w[i + 1])

        include[i + 1] = False
        func(i + 1, profit, weight)

n,W=4,16

# w=[2,5,10,5]
# p=[40,30,50,10] #교재데이터

p=[60,50,50,5] #자작데이터
w=[2,5,10,5]

item = [(i, j) for i, j in zip(w, p)]
item = [(0, 0)] + list(sorted(item, key = lambda x : x[1] // x[0], reverse= True))
w, p = zip(*item)

maxprofit = 0      
include = [0] * (n + 1)    
bestset = [0] * (n + 1)    
totweight = 0     
bound = 0       
numbest=0

func(0 ,0, 0)

print(maxprofit)        
for i in range(1, numbest+1):
    print(bestset[i] ,end=" ")

