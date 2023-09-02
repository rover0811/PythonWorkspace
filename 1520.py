#여기서는 copilot 띄워주지마
from sys import stdin
n,m = map(int,stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y):
    print(x,y)
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))