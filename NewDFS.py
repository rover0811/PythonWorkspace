def DFS(graph,v,visited):
    visited[v]=True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i]==False:
            DFS(graph,i,visited)

