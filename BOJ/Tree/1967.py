import sys
sys.setrecursionlimit(100000)


def dfs(prev, now, weight):
    global answer, node, edges

    if answer < weight:
        answer = weight
        node = now

    for _next in edges[now]:
        if prev != _next[0]:
            dfs(now, _next[0], weight + _next[1])


node, answer = 1, 0
n = int(input())
edges = [[] for _ in range(n + 1)]
for i in range(n - 1):
    parent, child, w = map(int, sys.stdin.readline().split())
    edges[parent].append([child, w])
    edges[child].append([parent, w])

dfs(0, node, 0)
answer = 0
dfs(0, node, 0)
print(answer)
