from sys import stdin

def divide(num, graph, width):

    if width == 2:
        for i in range(2):
            for j in range(2):
                graph[i][j] = num
                num+=1

        return
    else:
        divide(num,graph, width//2)



if __name__ == "__main__":
    N, r, c = map(int, stdin.readline().split())
    N = 2**N
    graph = [[0]*N for _ in range(N)]

    divide(0,graph,N)