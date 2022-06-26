# BFS는 너비 우선탐색
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다 -> 인자값은 2개
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번의 과정을 계속 수행

from collections import deque

def bfs(graph,start,visited):   #너는 왜 인자가 3개일까?
    queue=deque([start])          #넌 뭘까? # bfs는 함수를 여러번 실행하지 않는다 큐 형식으로 진행되니까.. 그냥 큐 만들어준거
    visited[start]=True              #넌 뭘까? start==|E| 원소의 개수만큼 방문 배열을 만들어준 것
    while queue:
        v=queue.popleft()       
        print(v,end=' ')         #왜 이렇게 할까? 파이썬의 기본은 end='\n'임
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

bfs(graph,1,visited)

