#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
from sys import stdin
from collections import deque
N, M, V= map(int, stdin.readline().split())

visited_bfs=[False]*(N+1)
visited_dfs=[False]*(N+1)


edge_list=[[] for i in range(N+1)]

# print(edge_list)

for i in range(M):
    a,b=map(int, stdin.readline().split())
    edge_list[b]+=[a]
    edge_list[a]+=[b]


for _ in edge_list:
    _.sort()

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph, start, visited):
    visited[start]=True
    print(start, end=" ")

    for node in graph[start]:
        if not visited[node] :
            dfs(graph,node,visited)


dfs(edge_list,V,visited_dfs)
print()
bfs(edge_list,V,visited_bfs)


