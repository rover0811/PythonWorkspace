from sys import stdin
from collections import deque


def bfs(x, y):

    count = 0
    queue = deque([(x, y)])
    graph[x][y] = 0

    directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    while queue:
        x, y = queue.popleft()

        for direction in directions:
            nx, ny = x+direction[0], y+direction[1]

            # 혹은 True?
            if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


if __name__ == '__main__':

    results=[]
    # n= int(stdin.readline())
    while True:
        n, m = map(int, stdin.readline().split())
        if n == 0 and m == 0:
            # print(result)
            for result in results:
                print(result)
            break

        # graph=[[int(k) for k in stdin.readline().rstrip("\n")] for i in range(n)]

        graph = [[*map(int, stdin.readline().split())] for i in range(m)]

        count = 0

        # print(graph)
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    bfs(i, j)
                    count += 1
        # print(count)
        results.append(count)
