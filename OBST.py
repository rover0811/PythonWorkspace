import sys
p = [0.375, 0.375, 0.125, 0.125]
n = len(p)  # 4
A = [[0] * (n + 1) for _ in range(n + 2)]  # 최소 비용 저장 6행 5열
R = [[0] * (n + 1) for _ in range(n + 2)]  # 최소 비용 저장 6행 5열


def minimum(A, p, i, j):
    minValue = sys.maxsize
    minK = 0
    for k in range(i, j+1):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]  # summation of p[m], 즉 지금까지 모든 k 서치값의 합
        if (minValue > value):
            minValue = value
            minK = k
    return minValue, minK  # 최소값 찾아서 반납


for i in range(1, n+1):
    # A[i][i - 1] = 0
    A[i][i] = p[i-1]
    # R[i][i - 1] = 0
    R[i][i] = i

A[n+1][n] = 0  # A[5][4]
R[n+1][n] = 0  # R[5][4]

for diag in range(1, n):
    for i in range(1, n-diag+1):
        j = i+diag
        A[i][j], R[i][j] = minimum(A, p, i, j)


for i in A:
    print(i)

print()
for i in R:
    print(i)
