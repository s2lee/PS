import sys


def dfs(x, cnt):
    if cnt == 4:
        print(1)
        sys.exit(0)

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


N, M = map(int, input().split())
visited = [False] * N
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
