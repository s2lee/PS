def dfs(v):
    global cnt
    visited[v] = True
    if graph[v]:
        for i in graph[v]:
            if not visited[i]:
                dfs(i)
    else:
        cnt += 1
        return


n = int(input())
parent = list(map(int, input().split()))
d = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    if parent[i] != -1:
        graph[parent[i]].append(i)
    else:
        root = i

for i in range(n):
    if d in graph[i]:
        graph[i].remove(d)

visited = [False] * (n + 1)
cnt = 0

if d != root:
    dfs(root)

print(cnt)
