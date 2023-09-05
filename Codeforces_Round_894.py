from sys import stdin

result = []
def find_letter(carpet, letter, start_num=0):
    for i in range(start, m):
        for j in range(n):
            if carpet[i][j] == letter:
                return i
    return -1

def transpose_matrix(matrix):
    # 행과 열의 개수를 구합니다.
    rows = len(matrix)
    cols = len(matrix[0])

    # 빈 리스트를 생성하여 행과 열을 바꾼 행렬을 저장할 준비를 합니다.
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # 행렬의 행과 열을 바꾸어 저장합니다.
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


t = int(stdin.readline())

for i in range(t):
    n,m = map(int,stdin.readline().split()) # n이 row의 갯수, m이 column의 갯수
    carpet = [[] for r in range(n)]
    for _ in range(n):
        carpet[_] = list(stdin.readline().strip())
    carpet= transpose_matrix(carpet)

    start = 0
    for letter in "vika":
        start=find_letter(carpet,letter,start_num=start)

        if start ==-1:
            result.append("NO")
            break
        elif start+1 == m and letter != "a": 
            result.append("NO")
            break
        elif start+1 == m and letter == "a":
            result.append("YES")
            break
        else:
            start += 1

[print(r) for r in result]
