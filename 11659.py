from sys import stdin
N,M=map(int,stdin.readline().split())

a=list(map(int,stdin.readline().split()))

subset=[map(int,stdin.readline().split()) for i in range(M)]

dp=[[0 for i in range(N+1)]for i in range(N+1)]

# for k in range(1,N+1):
#     for i in range(1,N+1):
#         print(k,i,end=" ")
#     print()
for diag in range(0, N):
    for i in range(1, N+1-diag):
        j = i+diag
        for k in range(i-1, j):
            dp[i][j]=a[k]

for diag in range(1, N):
    for i in range(1, N+1-diag):
        j = i+diag
        for k in range(i, j):
            dp[i][j]=dp[i][j-1]+dp[j][j]

for first,second in subset:
    print(dp[first][second])
