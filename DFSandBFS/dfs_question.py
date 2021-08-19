n, m = map(int, input().split())
graph = []
result = 0
z = 0

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        print("graph[",x,"][",y,"] = ",graph[x][y])
    global z
    z += 1
    if x <= -1 or x >= n or y <= -1 or y >= m:
        print("-------벗어나서 FALSE")
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    print("-------0이 아니라서 FALSE")
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            print("===>result 1추가 i : ", i, " j : ", j)
            result += 1

print(result)

