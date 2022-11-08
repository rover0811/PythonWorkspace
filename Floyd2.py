def path(P, q, r):
    q -= 1
    r -= 1
    if P[q][r] != 0:
        path(P, q+1, P[q][r])
        print(P[q][r], end=" ")
        path(P, P[q][r], r+1)


def floyd2(n, W, D, P):
    P = [[0]*n for _ in range(n)]
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(D[i][k]+D[k][j] < D[i][j]):
                    P[i][j] = k+1
                    D[i][j] = D[i][k]+D[k][j]
        print("W{0} 배열 출력".format(k+1))
        for i in W:  # 제출시 20행부터 25행까지 삭제할것
            print(i)
        print()
        print("P{0} 배열 출력".format(k+1))
        for i in P:
            print(i)
        print()

    print("D배열 출력")
    for i in D:
        print(i)
    print("\nP배열 출력")
    for i in P:
        print(i)
    print("\nPath 알고리즘 출력")
    path(P, 2, 5)


INF = 100
# a = [
#     [0, 1, INF, 1, 5],
#     [9, 0, 3, 2, INF],
#     [INF, INF, 0, 4, INF],
#     [INF, INF, 2, 0, 3],
#     [3, INF, INF, INF, 0]
# ] 교재 데이터
a = [
    [0, INF, 5, 8, INF],
    [7, 0, INF, INF, INF],
    [INF, 6, 0, INF, 3],
    [INF, INF, 4, 0, INF],
    [4, 10, INF, INF, 0]
]  # 자작 데이터
b = [[0]*5 for _ in range(5)]
c = 1
floyd2(5, a, b, c)
