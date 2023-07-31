from collections import deque

T=int(input())

def bfs(a,b):
    queue=deque([])
    queue.append((a,b))

    dx=[-1,1,0,0] #좌, 우, 상, 하
    dy=[0,0,-1,1]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=0 and nx<M and ny>=0 and ny<N and graph[nx][ny] ==1 :
                queue.append((nx,ny))
                graph[nx][ny] =0

            

    
    #초기값을 큐에 넣고

    #그 다음에 while문으로 큐가 다 비워질 때까지 돌리고

    #방문한 노드는 방문하지 않은 노드일 때, 다시 큐에 넣고, 방문했다고 체크

    #여기서 사각 그리드면 방향도 만들어줘야하는데


for _ in range(T):
    M,N,K=map(int,input().split()) # 가로, 세로, 배추가 심어져있는 개수

    graph=[[0]*N for k in range(M)]

    # print(graph)

    for j in range(K):
        a,b=map(int,input().split())
        graph[a][b]=1
    total=0
    for g in graph:
        print(g)
    for i in range(N): # 0 ,1, 2
        for j in range(M): # 0, 1 ,2, 3, 4, 5
            if graph[j][i]==1:
                bfs(j,i)
                total+=1


    print(total)
    

