from sys import stdin

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

n, m = map(int, stdin.readline().split())

board = [list(map(int, stdin.readline().split())) for _ in range(n)]

houses = []
chickens = []

for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            houses.append((x+1,y+1))
        elif board[x][y]==2:
            chickens.append((x+1,y+1))

            
chickens_count =len(chickens)

if m >= chickens_count:
    low = 0
    for x,y in houses:
        low += min([distance(x,y,cx,cy) for cx,cy in chickens])
    print(low)

else:
    from itertools import combinations
    chickens_candidate = combinations(chickens,m)
    low_candidate = []

    for chickens_selected in chickens_candidate:
        low = 0
        for hx,hy in houses:
            low += min([distance(hx,hy,cx,cy) for cx,cy in chickens_selected])
        low_candidate.append(low)
    
    print(min(low_candidate))
