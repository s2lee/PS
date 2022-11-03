import sys
sys.setrecursionlimit(100000)


def dfs(v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            tree.append((v, i))
            dfs(i, visited)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
tree = []
dfs(1, visited)
tree = sorted(tree, key=lambda x: x[1])
for x in tree:
    print(x[0])
