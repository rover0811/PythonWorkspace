# from sys import stdin
# n = int(stdin.readline())

# left_down_diagonal = [0 for _ in range(2*n-3)]
# right_up_diagonal = [0 for _ in range(2*n-3)]
# row = [0 for _ in range(n)]

# def dfs(y,new_chess_board):
#     if y == n: # 퀸을 다 배치했으면
#         return 1
#     result = 0
#     for loop_x in range(n):
#         if check(loop_x,y, new_chess_board): # 퀸을 놓을 수 있으면
#             new_chess_board = set_queen(loop_x,y)
#             result += dfs(y+1, new_chess_board) # 다음 퀸 배치
#     # 퀸을 놓을 수 없으면
#     return result

# # x는 행, y는 열
# def check(x,y,new_chess_board):

#     left_down_diagonal= new_chess_board[0] # 로컬
#     right_up_diagonal = new_chess_board[1] # 로컬
#     row = new_chess_board[2] # 로컬

#     left_down_index = y-x+n-2
#     right_up_index = 

#     if row[x] == -1 or left_down_diagonal[x+y] == -1 or right_up_diagonal[x-y+n-1] == -1:
#         return False
#     else:
#         return True

# def set_queen(x,y):
#     left_down_diagonal[x+y] = 1
#     right_down_diagonal[x-y+n-1] = 1
#     row[x] = 1

#     return left_down_diagonal, right_down_diagonal, row

n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
