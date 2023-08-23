from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

n = int(stdin.readline())

edges = [tuple(map(int,stdin.readline().split())) for i in range(n-1)]

adj_list = [[] for i in range(n+1)]

for k,v in edges:
    adj_list[k].append(v)
    adj_list[v].append(k)

visited = [False for i in range(n+1)]

#[[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

def dfs(prev,now):
    visited[now] = True
    now_you_go = [*adj_list[now]]
    adj_list[now] = prev
    for i in now_you_go:
        if visited[i] == False:
            dfs(now,i)


dfs(1,1)

for i in adj_list[2:]:
    print(i)
