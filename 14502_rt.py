# 1. 벽 세우기
# 2. 바이러스 퍼트리기
# 3. 안전영역 구하기
# 4. 얻을 수 있는 안전영역의 최대값 구하기
# 5. 안전영역의 정의는 전체 크기에서 바이러스와 벽이 차지하는 영역을 뺀 값




from sys import stdin
from collections import deque
from itertools import combinations


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = dx + x
            ny = dy + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))


def check_graph(graph, n, m):

    zero_list = []
    virus_list = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                zero_list.append((i, j))
            elif graph[i][j] == 2:
                virus_list.append((i, j))

    return zero_list, virus_list



# 이 코드의 시간복잡도는?

# 1. check_graph : O(n^2)
# 2. combinations : O(n^3)
# 3. bfs : O(n^2)
# 4. max : O(n^2)
# 5. sum : O(n^2)
# 6. print : O(1)
# 7. total : O(n^3)

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    graph = [[int(k) for k in stdin.readline().split()] for i in range(n)]

    zero_list, virus_list = check_graph(graph,n,m)

    wall_list = list(combinations(zero_list,3))

    temp_safe_area=0

    for wall in wall_list:
        temp_graph = [item[:] for item in graph] # deep copy라고 할 수 있니? # copy.deepcopy(graph)로도 가능 # 이게 대신 빠르지 않나? 

        for x,y in wall:
            temp_graph[x][y] = 1

        for x,y in virus_list:
            bfs(temp_graph,x,y)
        
        temp_safe_area = max(temp_safe_area, sum(i.count(0) for i in temp_graph))

    print(temp_safe_area)