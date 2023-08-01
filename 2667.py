from sys import stdin
from collections import deque


def bfs(x,y):
    
    count =0
    queue=deque([(x,y)])
    graph[x][y]=0

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while queue:
        x, y = queue.popleft()
        #graph[x][y]= 0 # 처리를 해줘야 하는데 아무래도 그래프에서 그냥 매기지 않을까? 공간 낭비인가?

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 혹은 True?
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                # graph[nx][ny]+=graph[x][y]
                graph[nx][ny] = 0
                count+=1

    return count





if __name__ == '__main__':

    n= int(stdin.readline())
    graph=[[int(k) for k in stdin.readline().rstrip("\n")] for i in range(n)]

    result=[]

    # print(graph)
    for i in range(n):
        for j in range(n):
            # count=bfs(i,j)
            if graph[i][j]==1:
                result.append(bfs(i,j)+1)
    
    result.sort()

    print(len(result))
    for i in result:
        print(i)


