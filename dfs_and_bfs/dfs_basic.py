'''
DFS example
'''

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)




