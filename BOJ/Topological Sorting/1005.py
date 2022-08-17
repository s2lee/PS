from collections import deque
import copy


for _ in range(int(input())):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    W = int(input())
    dp = copy.deepcopy(time)
    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            dp[i] = max(dp[i], dp[now] + time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    print(dp[W])
