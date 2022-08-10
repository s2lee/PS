n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = [(start, 0)]
    visited = [0] * (n + 1)
    while q:
        cur, cnt = q.pop(0)
        for x in graph[cur]:
            if not visited[x]:
                visited[x] = cnt + 1
                q.append((x, cnt + 1))

    return sum(visited)


min_value = 1e9
ans = -1
for i in range(1, n + 1):
    sum_value = bfs(i)
    if sum_value < min_value:
        min_value = sum_value
        ans = i

print(ans)
