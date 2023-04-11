import sys
sys.setrecursionlimit(10000)

N,edge_num=map(int,sys.stdin.readline().rstrip().split())
# edge_num=int(input())

edge_list=[tuple(map(int, sys.stdin.readline().rstrip().split())) for i in range(edge_num)]
visited_list=[False]*(N+1)
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# print(edge_list)
edge_overlap_list=[[] for i in range(N+1)]
for k in edge_list:
    edge_overlap_list[k[0]].append(k[1])
    edge_overlap_list[k[1]].append(k[0])

# print(edge_overlap_list)


# dfs(edge_overlap_list,1,visited_list)

count=0

for i in range(1,N+1):
    if visited_list[i]==False:
        count+=1
        dfs(edge_overlap_list,i,visited_list)
print(count)
# print(visited_list)
