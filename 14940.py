from collections import deque
from sys import stdin


#여기서 틀린게 있나?
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            #벽이면 무시
            if graph[nx][ny] == 0:
                continue

            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                visited[nx][ny] = True
                queue.append((nx,ny))


if __name__ == "__main__":

    #내가 입력 받는 코드보다 더 효율적인 방법이 있니?
    
    N, M = map(int, stdin.readline().split())
    graph = [[*map(int,stdin.readline().split())] for _ in range(N)]
    visited = [[False]*M for _ in range(N)]


    project=[(x,y) for x in range(N) for y in range(M) if graph[x][y] == 2]

    # print(project)
    
    for x,y in project:
        graph[x][y] = 0
        bfs(x,y)
    
    for x in range(N):
        for y in range(M):
            if visited[x][y] == False and graph[x][y] != 0:
                graph[x][y] = -1

    for row in graph:
        print(*row)