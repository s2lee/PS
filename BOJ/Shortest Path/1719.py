N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [[0] * (N + 1) for _ in range(N + 1)]

for a in range(N + 1):
    for b in range(N + 1):
        if a == b:
            graph[a][b] = 0
            ans[a][b] = INF

for _ in range(M):
    v1, v2, route = map(int, input().split())
    graph[v1][v2] = route
    graph[v2][v1] = route
    ans[v1][v2] = v2
    ans[v2][v1] = v1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                ans[a][b] = ans[a][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ans[i][j] == INF:
            print('-', end=' ')
        else:
            print(ans[i][j], end=' ')
    print()
