n, m = map(int, input().split())
INF = float("inf")
graph = [[] for _ in range(n + 1)]
dist = [INF for _ in range(n + 1)]
dist[1] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

for cnt in range(1, n + 1):
    for s in range(1, n + 1):
        for e, w in graph[s]:
            if dist[e] > dist[s] + w:
                dist[e] = dist[s] + w
                if cnt == n:
                    print(-1)
                    exit()

for i in range(2, n + 1):
    print(-1) if dist[i] == INF else print(dist[i])
