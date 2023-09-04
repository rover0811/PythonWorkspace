# 트리의 지름 쉬운 버전
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

n = int(stdin.readline())

edge_list = [tuple(map(int, stdin.readline().split())) for i in range(n-1)]

# 부모, 자식, 가중치
# [(1, 2, 3), (1, 3, 2), (2, 4, 5), (3, 5, 11), (3, 6, 9), (4, 7, 1), (4, 8, 7), (5, 9, 15), (5, 10, 4), (6, 11, 6), (6, 12, 10)]

# 여기서 나는 인접 행렬 또는 인접 리스트로 만들어야한다. n 이 10000개 이하이므로 나는 인접 리스트를 택하겠다.

adj_list = [[] for i in range(n+1)] # 첫번째 칸 비우려고 +1

for parent, children, weight in edge_list:
    adj_list[parent].append((children, weight))
    adj_list[children].append((parent,weight))

visited = [False]*(n+1)

# adj_list
# [[], [(2, 3), (3, 2)], [(4, 5)], [(5, 11), (6, 9)], [(7, 1), (8, 7)], [(9, 15), (10, 4)], [(11, 6), (12, 10)], [], [], [], [], [], []]

# new_adj_list
# [[], [(2, 3), (3, 2)], [(1, 3), (4, 5)], [(1, 2), (5, 11), (6, 9)], [(2, 5), (7, 1), (8, 7)], [(3, 11), (9, 15), (10, 4)], [(3, 9), (11, 6), (12, 10)], [(4, 1)], [(4, 7)], [(5, 15)], [(5, 4)], [(6, 6)], [(6, 10)]]

# 1 [(2, 3), (3, 2)]
# 2 [(1, 3), (4, 5)]
# 4 [(2, 5), (7, 1), (8, 7)]
# 7 [(4, 1)]
def dfs(prev, temp, sum):
    global max_len
    global max_len_node

    visited[temp] = True

    for node, weight in adj_list[temp]:
        if visited[node] == False:
            dfs(temp, node, sum+weight)

    if len(adj_list[temp]) == 1: # 말단까지 내려왔다는 것을 어떻게 알 수 있을까? 리스트 길이가 1이면 말단이다
        if sum > max_len:
            max_len = sum
            max_len_node=temp


max_len = 0
max_len_node=0
        

dfs(1,1,0)

total = max_len
last_node = max_len_node
max_len = 0
max_len_node=0
visited = [False]*(n+1)

dfs(last_node,last_node,0)

print(max_len)
