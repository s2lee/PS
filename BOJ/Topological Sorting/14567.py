from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append((i, 1))

    while q:
        now, min_com = q.popleft()
        result.append((now, min_com))
        min_com += 1
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append((i, min_com))

    for x in sorted(result):
        print(x[1], end=" ")


topology_sort()