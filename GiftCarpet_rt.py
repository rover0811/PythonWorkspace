from sys import stdin

def is_vika(carpet):
    for i in range(n):
        for j in range(m):
            if carpet[i][j] == "v":
            if i+1 < n and carpet[i+1][j] == "i":
            if i+2 < n and carpet[i+2][j] == "k":
            if i+3 < n and carpet[i+3][j] == "a":
                            return True
    return False

t = int(stdin.readline())
n, m = map(int,stdin.readline().split()) # n이 row의 갯수, m이 column의 갯수
carpet = [[] for r in range(t)]

for i in range(t):
    carpet[i].append(list(stdin.readline().strip()))

print(carpet)
