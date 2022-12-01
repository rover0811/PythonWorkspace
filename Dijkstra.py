INF = 1000


def dijkstra(n, W, F):
    touch = [1] * (n+1)  # 1번 노드에서 시작합니다.
    length = [1] * (n+1)
    for i in range(2, n+1):
        length[i] = W[1][i]  
    # print(length)
    for i in range(1, n):
        min = INF
        for j in range(2, n+1):
            if 0 <= length[j] < min:
                min = length[j]
                vnear = j  
        F.append((touch[vnear], vnear))
        for k in range(2, n+1):
            if length[vnear] + W[vnear][k] < length[k]:
                length[k] = length[vnear] + W[vnear][k]
                touch[k] = vnear

        length[vnear] = -1

    return F


# a = [# 교재 데이터
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 7, 4, 6, 1],
#     [0, INF, 0, INF, INF, INF],
#     [0, INF, 2, 0, 5, INF],
#     [0, INF, 3, INF, 0, INF],
#     [0, INF, INF, INF, 1, 0]
# ]
a = [ ## 자작데이터
    [0, 0, 0, 0, 0, 0],
    [0, 0, 10, 5, 6, 2],
    [0, INF, 0, INF, INF, INF],
    [0, INF, 6, 0, 4, INF],
    [0, INF, 2, INF, 0, INF],
    [0, INF, INF, INF, 3, 0]
]
b = []
F = []
F = dijkstra(5, a, b)

print(F)
