import sys


def optsearchtree(p):
    n = len(p)-1
    A = [[0] * (n + 2) for _ in range(n + 2)]  # 최소 비용 저장
    R = [[0] * (n + 2) for _ in range(n + 2)]  # 루트노드를 저장함
    for i in range(0, n + 1):
        A[i+1][i] = 0
        A[i+1][i+1] = p[i]
        R[i+1][i+1] = 0
        R[i+1][i] = i  # 한개밖에 없으면 자기 자신이 루트임
        # 초기화 과정
    A[n + 1][n] = 0
    R[n + 1][n] = 0
    for diagonal in range(1, n):  # 대각선을 중심대각선부터 마지막 대각선까지 반복함
        for i in range(1, n - diagonal + 1):  # 대각선 안에서의 이동
            j = i + diagonal  # 현재 diagonal에서 몇번째 원소인지를 결정함, 1번 대각선은 이미 자기자신으로 설정되어있음
            A[i][j], R[i][j] = minimum(A, p, i, j)
    return A, R


def minimum(A, p, i, j):
    minValue = sys.maxsize
    minK = 0
    for k in range(i-1, j):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]  # summation of p[m], 즉 지금까지 모든 k 서치값의 합
        if (minValue > value):
            minValue = value
            minK = k
    return minValue, minK  # 최소값 찾아서 반납


a, b = optsearchtree([0, 0.375, 0.375, 0.125, 0.125])

for i in a:
    print(i)
print()
for i in b:
    print(i)
