def dfs(v, visited, d):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            d[i] = d[v] + 1
            dfs(i, visited, d)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

d = [0] * (n + 1)
visited = [False] * (n + 1)
dfs(a, visited, d)
if not visited[b]:
    print(-1)
else:
    print(d[b])
