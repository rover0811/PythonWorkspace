# 1 ,2 ,3 더하기
from sys import stdin
t = int(stdin.readline())

n = [int(stdin.readline()) for i in range(t)]

dp = [0 for i in range(12)] # 이 dp 배열의 1,2,3번째 인덱스는 1,2,3을 만드는 경우의 수이다.

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in n:
    print(dp[i])
