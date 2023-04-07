from collections import deque
N,M=map(int,input().split())

graph=[list(map(int,list(input()))) for i in range(N)]

for i in graph:
    print(i)


def dfs_drink(x,y):
    if x<-1 or x>=N or y<=-1 or y>=M:
        return False
    print(x,y)
    if graph[x][y]==0:
        graph[x][y]=1
        dfs_drink(x+1,y)# 우
        dfs_drink(x,y-1)# 하
        dfs_drink(x-1,y)# 좌
        dfs_drink(x,y+1)# 상
        return True
    return False


result=0
for i in range(N):
    for k in range(M): 
        if dfs_drink(i,k)==True:
            result+=1

print(result)


        
