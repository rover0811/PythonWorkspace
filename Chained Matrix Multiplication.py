import sys
n = 6  # 행렬 개수
d = [7, 4, 2, 6, 3, 5, 8]
M = [[0 for x in range(n+1)] for y in range(n+1)]
P = [[0 for x in range(n+1)] for y in range(n+1)]


def ChainedMatrix(M, P, n, d, NUM1, NUM2):
    for diag in range(1, n):
        for i in range(1, n+1-diag):
            j = i+diag
            M[i][j] = sys.maxsize
            for k in range(i, j):  # minimum 부분
                temp = min(M[i][j], M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j])
                if (M[i][j] > temp):
                    M[i][j] = temp
                    P[i][j] = k
    print("W배열:")
    for i in M:
        print(i)
    print()
    print("P배열:")
    for i in P:
        print(i)
    print("\nM[{0}][{1}] 출력:".format(NUM1, NUM2))
    print(M[NUM1][NUM2])


def order(P, i, j):
    if(i == j):
        print("A%d" % (i), end=' ')
    else:
        k = P[i][j]
        print("(", end='')
        order(P, i, k)
        order(P, k+1, j)
        print(")", end='')


# def order2(P, i, j):
#     if(i == j):
#         # print("A%d" % (i), end=' ')
#         pass
#     else:
#         k = P[i][j]
#         # print("(", end='')
#         print("order({0},{1})".format(i, k))
#         order2(P, i, k)
#         print("order({0},{1})".format(k+1, j))
#         order2(P, k+1, j)
#         # print(")", end='')


ChainedMatrix(M, P, n, d, 1, 6)
print("\norder 알고리즘 출력:")
order(P, 1, 6)
