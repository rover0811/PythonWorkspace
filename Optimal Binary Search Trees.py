def minimum(A, p, i, j):
    minValue = 999
    minK = 0
    for k in range(i, j + 1):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]
        if (minValue > value):
            minValue = value
            minK = k

    return minValue, minK


def optsearchtree(p):  # p=[0, 0.375, 0.375, 0.125, 0.125]
    n = len(p) - 1     # n=4
    A = [[0] * (n + 2) for _ in range(n + 2)]  # 6*6 행렬 생성
    R = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):  # i=1,2,3,4
        A[i][i - 1] = 0
        A[i][i] = p[i]
        R[i][i - 1] = 0
        R[i][i] = i
    A[n + 1][n] = 0
    R[n + 1][n] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            A[i][j], R[i][j] = minimum(A, p, i, j)

    return A, R


# 자작데이터 [0, 0.25, 0.25, 0.375, 0.125]
A, R = optsearchtree([0, 0.25, 0.25, 0.375, 0.125])
for i in A:
    print(i)
print()
for i in R:
    print(i)
