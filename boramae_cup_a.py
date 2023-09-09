# 마크는 세로 Y칸, 가로 X칸의 크기이며, 좌우 대칭이어야 한다.
# 각 칸은 흰색, 노란색, 파란색 중 하나로 색칠해야 하며, 특히 테두리는 파란색으로 칠해야 한다.
# 어떤 색의 문양이란, 해당 색으로 색칠된 인접한 칸들의 묶음이다. 두 칸이 변을 공유하는 경우에 두 칸은 인접한다고 정의한다.
# 마크 안엔 정확히 2개의 흰색 문양, 1개의 노란색 문양, 그리고 1개의 파란색 문양이 있어야 한다.
# 두 흰색 문양은 중앙을 기준으로 서로 좌우 대칭 관계여야 한다.
# 모든 흰색 문양은 노란색 문양과 한 칸 이상 변을 공유해야 한다.


def print_board(board):
    for row in board:
        for elem in row:
            print(elem, end='')
        print()

def is_symmetry(board):
    if x%2 == 0: # 짝수면
        left_board = [board[i][:x//2] for i in range(y)]
        right_board = [board[i][x//2:] for i in range(y)]
        reversed_right_board = [right_board[i][::-1] for i in range(y)]

        if left_board == reversed_right_board:
            return True
        else:
            return False
    else:
        left_board = [board[i][:x//2] for i in range(y)]
        right_board = [board[i][x//2+1:] for i in range(y)]
        reversed_right_board = [right_board[i][::-1] for i in range(y)]

        if left_board == reversed_right_board:
            return True
        else:
            return False
def make_boundary_blue(board):
    
        for elem in board[0]:
            if elem == "X":
                elem = "B"
            
        for elem in board[-1]:
            if elem == "X":
                elem = "B"
        
        for i in range(y):
            if board[i][0] == "X":
                board[i][0] = "B"
            if board[i][-1] == "X":
                board[i][-1] = "B"
        
def is_boundary_blue(board):

    for elem in board[0]:
        if elem != "B":
            return False
        
    for elem in board[-1]:
        if elem != "B":
            return False
    
    for i in range(y):
        if board[i][0] != "B":
            return False
        if board[i][-1] != "B":
            return False
        
    return True

def where_is_blank(board):

    blank_list = []

    for i in range(y):
        for j in range(x):
            if board[i][j] == "X":
                blank_list.append((i, j))
    
    return blank_list

def make_blue_symmetry(board):

    for idx,row in enumerate(board):
        reversed_row = row[::-1]
        if row == reversed_row:
            continue
        else:
            temp_row = row[:]

            for i in range(len(temp_row)):
                if temp_row[i] == "X" and reversed_row[i] == "B":
                    temp_row[i] = "B"
            board[idx]= temp_row

def divide_by_yellow(board,blank_list):

    # 노란색 문양이 중앙에 오는지 체크해야함
    # 홀수, 짝수 구분

    if x%2 == 0: # 짝수
        for blank in blank_list: # 최대한 중앙의 선에 있는 애들을 노랑으로 채움
            if blank[1] == x//2 or blank[1] == x//2-1:
                if board[blank[0]][blank[1]] == "X" and board[blank[0]][x-blank[1]-1] == "X":
                    board[blank[0]][blank[1]] = "Y"
                    # 반대편도 대칭으로 y로 바꿔줘야함
                    board[blank[0]][x-blank[1]-1] = "Y"
            else:
                board[blank[0]][blank[1]] = "W"
    else:
        for blank in blank_list: # 최대한 중앙의 선에 있는 애들을 노랑으로 채움
            if blank[1] == x//2:
                if board[blank[0]][blank[1]] == "X":
                    board[blank[0]][blank[1]] = "Y"
            else:
                board[blank[0]][blank[1]] = "W"




if __name__ == '__main__':
    y, x = map(int, input().split()) # 8, 16
    input_board = [list(input()) for _ in range(y)]

    make_boundary_blue(input_board)
    make_blue_symmetry(input_board)

    if is_symmetry(input_board) and is_boundary_blue(input_board):
        pass
    else:
        print("NO")
        exit()
    
    blank_list = where_is_blank(input_board)

    if len(blank_list) <= 2:
        print("NO")
        exit()
    

    divide_by_yellow(input_board,blank_list)

    # 6번 yellow랑 white랑 인접해있는지 체크하는 부분이 없네!

    if is_symmetry(input_board):
        print("YES")
        print_board(input_board)
    else:
        print("NO")
        exit()
    
    

    

    

        