from sys import stdin
from collections import deque


def read():
    global n, m
    n, m = map(int, stdin.readline().split())
    return [[int(k) for k in stdin.readline().rstrip("\n")] for i in range(n)]


graph = read()  # 인접행렬 방식으로 만들어진 거인가?

def bfs(a,b):

    queue = deque([])
    queue.append((a, b))  # 처음 자리 1,1 자리

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while queue:
        x, y = queue.popleft()
        #graph[x][y]= 0 # 처리를 해줘야 하는데 아무래도 그래프에서 그냥 매기지 않을까? 공간 낭비인가?

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 혹은 True?
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny]+=graph[x][y]

    return graph[n-1][m-1]
            

print(bfs(0,0))
