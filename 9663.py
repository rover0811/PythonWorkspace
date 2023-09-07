# N-queen 문제
from sys import stdin
n = int(stdin.readline())

chess_board = [[0 for _ in range(n)] for _ in range(n)] # chess_board 0으로 초기화 

# 백트래킹을 사용한 코드

def dfs(y, chess_board):
    if y == n: # 퀸을 다 배치했으면
        return 1
    result = 0
    for i in range(n):
        if chess_board[i][y] == 0: # 퀸을 놓을 수 있으면
            temp_chess_board = set_queen(i,y,chess_board)
            result += dfs(y+1,temp_chess_board) # 다음 퀸 배치
    # 퀸을 놓을 수 없으면
    return result


# x는 행, y는 열

def set_queen(x,y,t_chess_board):

    # print("x,y: ",x,y)
    # print("t_chess_board: ",t_chess_board)
    # chess_board를 깊은 복사해서 사용해야 한다.
    l_chess_board = [i[:] for i in t_chess_board]
    l_chess_board[x][y] = 1 # 퀸 배치

    # y열 다음 가로를 모두 -1 처리 -> 요건 ok
    for i in range(y+1,n):
        l_chess_board[x][i] = -1
        # print("x,y turn -1: ",x,i)
    
    # x,y 이후 좌하향하는 대각선을 모두 -1 처리
    temp_x = x
    temp_y = y
    while(temp_x<n-1 and y<n-1):
        temp_x += 1
        temp_y += 1
        if temp_x >= n or temp_y >= n:
            break
        l_chess_board[temp_x][temp_y] = -1
        # print("x,y turn -1: ",temp_x,temp_y)
    
    # x,y 이후 우상향하는 대각선을 모두 -1 처리
    temp_x = x
    temp_y = y

    while(temp_x>0 and temp_y<n-1):
        temp_x -= 1
        temp_y += 1
        if temp_x < 0 or temp_y >= n:
            break
        l_chess_board[temp_x][temp_y] = -1
        # print("x,y turn -1: ",temp_x,temp_y)


    # for row in range(x+1,n):
    #     for col in range(y+1,n):
    #         l_chess_board[row][col] = -1
    #         print("x,y turn -1: ",row,col)

    
    # # x,y 이후 우상향하는 를 모두 -1 처리
    # for row in range(x-1,-1,-1): # x가 0일 때까지
    #     for col in range(y+1,n): # y가 n-1일 때까지
    #         l_chess_board[row][col] = -1
    
    # print("l_chess_board: ",l_chess_board)

    return l_chess_board


print(dfs(0,chess_board))
