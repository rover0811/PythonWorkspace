from sys import stdin
from collections import deque


def bfs(x, y):

    count = 0
    queue = deque([(x, y)])
    # graph[x][y] = 0

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while queue:
        x, y = queue.popleft()
        # graph[x][y]= 0 # 처리를 해줘야 하는데 아무래도 그래프에서 그냥 매기지 않을까? 공간 낭비인가?

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 혹은 True?
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    count += 1
                    queue.append((nx, ny))
                # graph[nx][ny]+=graph[x][y]
                # count += 1

    return count



def find_zero(graph) -> list:

    result = []

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                result.append((i, j))
            elif graph[i][j] == 2:
                birus_list.append((i,j))


    return result


def combination_3(n) -> list:

    # nC3 을 구현 근데 쓸모가 없네 ㅋㅋ

    candidate = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                candidate.append((i, j, k))

    return candidate


if __name__ == '__main__':

    n, m = map(int, stdin.readline().split())
    graph = [[int(k) for k in stdin.readline().split()] for i in range(n)]

    birus_list = []
    zero_list = find_zero(graph)
    cap = len(zero_list)

    # print(birus_list)
    # print(zero_list)
    result=[]

    for i in range(cap-2):
        x_1, y_1 = zero_list[i]
        graph[x_1][y_1] = 1
        for j in range(i+1, cap-1):
            x_2, y_2 = zero_list[j]
            graph[x_2][y_2] = 1
            for k in range(j+1, cap):
                x_3, y_3 = zero_list[k]
                graph[x_3][y_3] = 1
                # print(zero_list[i], zero_list[j], zero_list[k])
                for x,y in birus_list:
                    # result.append(bfs(x,y))

                    if bfs(x,y)>0:
                        print(bfs(x,y))
                # 여기서 bfs 먹이기
                graph[x_3][y_3] = 0
            graph[x_2][y_2] = 0
        graph[x_1][y_1] = 0
    
    # print(min(result))


    # print(result)

    # for i in range(n):
    #     for j in range(n):
    #         if graph[i][j]==1:
    #             bfs(i,j)
