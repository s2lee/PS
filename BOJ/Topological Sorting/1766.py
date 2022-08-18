import sys
import heapq


N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    in_degree[B] += 1

h, result = [], []
for i in range(N + 1):
    if in_degree[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    result.append(now)

    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(h, i)

print(*result[1:])
