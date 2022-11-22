import sys
sys.setrecursionlimit(200000)

n, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

graph[0].append([r, 0])
graph[r].append([0, 0])
path = [0, r]
ans = 0
while (len(graph[path[-1]]) < 3) and (len(path) < n + 1):
    for _next, d in graph[path[-1]]:
        if _next != path[-2]:
            ans += d
            path.append(_next)
            break


def solve(cur, prv):
    res = 0
    for _next, d in graph[cur]:
        if _next != prv:
            res = max(res, solve(_next, cur) + d)
    return res


print(ans, solve(path[-1], path[-2]))
