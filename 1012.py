'''from sys import stdin
from collections import deque

directions_list=[(1,0),(0,1),(-1,0),(0,-1)] # 우, 하, 좌, 상

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v= queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

T=int(stdin.readline())

for _ in range(T):
    M,N,K=map(int,stdin.readline().split())

    coordinate_list=[]

    for t in range(K):
        coordinate_list.append(tuple(map(int,stdin.readline().split())))

    print(coordinate_list)

    # coordinate_list=[tuple(map(int,stdin.readline().split())) for _ in range(K)]

    # print(coordinate_list)'''

from collections import deque
def bfs(a,b):
    q=deque([])
    q.append((a,b))
    graph[a][b]=0 #visited!
    dx=[-1,1,0,0] #좌, 우, 상, 하
    dy=[0,0,-1,1]
    # bechu = 0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=0
t = int(input())
for _ in range(t):
    #초기화
    m,n,k = map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    total_num = 0

    #여기부터 입력 받는 부분
    for i in range(k):
        x,y = map(int,input().split())
        graph[y][x]=1

    #BFS 하는 부분
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)
                total_num+=1
    print(total_num)





    






