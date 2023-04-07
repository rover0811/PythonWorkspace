N=int(input())
edge_num=int(input())

edge_list=[tuple(map(int, input().split())) for i in range(edge_num)]
visited_list=[False]*(N+1)
count=0
def dfs(graph,v,visited):
    visited[v]=True
    global count
    count+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# print(visited_list)
edge_overlap_list=[[] for i in range(N+1)]
for k in edge_list:
    edge_overlap_list[k[0]].append(k[1])
    edge_overlap_list[k[1]].append(k[0])

# print(edge_overlap_list)


dfs(edge_overlap_list,1,visited_list)

print(count-1)



