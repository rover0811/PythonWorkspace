from itertools import combinations

N,M=map(int,input().split())

card=tuple(map(int,input().split()))

a=sorted([sum(i) for i in list(combinations(card,3))],reverse=True)

for index,value in enumerate(a):
    if value<=M:
        print(value)
        break

