'''
DFS example
'''
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    print(len(queue))
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 연결된 노드의 정보를 2차원 리스트로 표현
graph = [
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

# 각 노드의 방문 여부 정보를 1차원 리스트로 표현
visited = [False] * 9

bfs(graph, 1, visited)




