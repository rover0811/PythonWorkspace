# N=int(input())
# edge_num=int(input())

# edge_list=[tuple(map(int, input().split())) for i in range(edge_num)]
# visited_list=[False]*(N+1)
# count=0
# def dfs(graph,v,visited):
#     visited[v]=True
#     global count
#     count+=1
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# # print(visited_list)
# edge_overlap_list=[[] for i in range(N+1)]
# for k in edge_list:
#     edge_overlap_list[k[0]].append(k[1])
#     edge_overlap_list[k[1]].append(k[0])

# # print(edge_overlap_list)


# dfs(edge_overlap_list,1,visited_list)

# print(count-1)

from collections import deque

def bfs(graph,start,visited):
    counter=0
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        # print(v,end=" ")
        counter+=1

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    
    return counter

N=int(input())
edge_num=int(input())

edge_list=[tuple(map(int, input().split())) for i in range(edge_num)]

new_edge_list=[[] for _ in range(N+1)]

for edge in edge_list:
    new_edge_list[edge[0]]+=[edge[1]]
    new_edge_list[edge[1]]+=[edge[0]]


visited=[False]*(N+1)

print(bfs(new_edge_list,1,visited)-1)

# from collections import deque
# n=int(input()) # 컴퓨터 개수
# v=int(input()) # 연결선 개수
# graph = [[] for i in range(n+1)] # 그래프 초기화
# visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
# for i in range(v): # 그래프 생성
#     a,b=map(int,input().split())
#     graph[a]+=[b] # a에 b 연결
#     graph[b]+=[a] # b에 a 연결 -> 양방향
# visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시

# print(graph)


# Q=deque([1])
# while Q:
#     c=Q.popleft()
#     for nx in graph[c]:
#         if visited[nx]==0:
#             Q.append(nx)
#             visited[nx]=1
# print(sum(visited)-1)





