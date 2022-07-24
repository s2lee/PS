from collections import deque


def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_count = 0
for i in range(1, n + 1):
    count = bfs(i)
    if count > max_count:
        result = [i]
        max_count = count
    elif count == max_count:
        result.append(i)
        max_count = count

print(*result)
