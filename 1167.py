from sys import stdin

def make_edge(input_list: list):
    output = []
    for i in range(1,len(input_list)):
        if i%2 ==1:
            output.append((input_list[0],input_list[i],input_list[i+1]))
        elif i%2 ==0 and input_list[i+1] == -1:
            break
    return output


n = int(stdin.readline())

edge_lists = [make_edge(list(map(int, stdin.readline().split())))
              for i in range(n)]

edge_lists.insert(0,[])

# def dfs(graph, i):
#     for j in graph[i]:
#         if not visited[j]:
#             dfs(graph, j)

def dfs(prev, temp):

    for j in edge_lists[temp]:
        if prev != temp:
            dfs()



