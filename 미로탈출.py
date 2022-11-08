from asyncio.format_helpers import _get_function_source
from collections import deque
import queue

N,M=map(int, input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))
# visited=[N][M]

# for i in N:
#     for k in M:
#         visited[N][M]=False

# def bfs(gragh,start,visited):
#     queue=deque([start])
#     visited[start]=True
#     while queue:
#         v=queue.popleft

def hi(graph):
    i=0
    j=0
    count=0
    queue=deque(1)
    while queue:
        queue.popleft
        if(graph[i][j+1]): #우
            queue.append(graph[i][j+1])
            j+=1
            count+=1
            continue
        elif(graph[i+1][j]): #하
            queue.append(graph[i+1][j])
            i+=1
            count+=1
            continue
        elif(graph[i-1][j]): #상
            queue.append(graph[i-1][j])
            i+=1
            count+=1
            continue
        elif(graph[i][j-1]): #좌
            queue.append(graph[i][j-1])
            i+=1
            count+=1
            continue
        else:
            return count

print(hi(graph))

                

