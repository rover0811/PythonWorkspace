import sys
N,M=map(int,sys.stdin.readline().split()) #N은 나무의 수, M은 가져가고픈 나무의 길이

a=sorted(list(map(int,sys.stdin.readline().split()))) #나무들

min=min(a)
max=max(a)
mid=(min+max)//2

print(min,max)

take=0

for i in a:
    if i<=mid:
        pass
    else:
        take+=i-mid

print(take) #min 22 max 0 mid 7


    
