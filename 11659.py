

'''
    방법 1: 슬라이싱으로 풀기 -> 바보
'''



# for k in range(1,N+1):
#     for i in range(1,N+1):
#         print(k,i,end=" ")
#     print()

'''

    방법 2: DP로 풀어보기
'''

# from sys import stdin
# N,M=map(int,stdin.readline().split())

# a=list(map(int,stdin.readline().split()))
# subset=[map(int,stdin.readline().split()) for i in range(M)]
# subset=[map(int,stdin.readline().split()) for i in range(M)]

# dp=[[0 for i in range(N+1)]for i in range(N+1)]
# for diag in range(0, N):
#     for i in range(1, N+1-diag):
#         j = i+diag
#         for k in range(i-1, j):
#             dp[i][j]=a[k]

# for diag in range(1, N):
#     for i in range(1, N+1-diag):
#         j = i+diag
#         for k in range(i, j):
#             dp[i][j]=dp[i][j-1]+dp[j][j]

# for first,second in subset:
#     print(dp[first][second])


'''
    방법 3: 앞, 끝만 처리하기 
'''

from sys import stdin
N,M=map(int,stdin.readline().split())

a=list(map(int,stdin.readline().split()))
rangelist=[map(int,stdin.readline().split()) for i in range(M)]

subsetlist=[0]
for index,value in enumerate(a):
    subsetlist.append(subsetlist[index]+value)

for start,end in rangelist:
    print(subsetlist[end]-subsetlist[start-1])

