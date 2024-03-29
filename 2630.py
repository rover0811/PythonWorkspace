# 색종이 만들기

from sys import stdin
n = int(stdin.readline())
paper = [list(map(int,stdin.readline().split())) for i in range(n)]

white = 0
blue = 0

def cut(x,y,n):
    global white,blue
    check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1

def solution():
    global white,blue
    cut(0,0,n)
    print(white)
    print(blue)

solution()