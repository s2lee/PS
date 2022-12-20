import sys
input = sys.stdin.readline


N = int(input())
nodes = [0] + [[] for _ in range(N)]
visit = [0] * (N + 1)
dp = [[0 for _ in range(N + 1)], [1 for _ in range(N + 1)]]
for i in range(N - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

que = [1]

while que:
    crt = que[-1]
    crt_state = 1
    if not visit[crt]:
        visit[crt] = 1
        for i in nodes[crt]:
            if not visit[i]:
                que.append(i)
                crt_state = 0
    if crt_state:
        crt = que.pop()
        visit[crt] = -1
        for i in nodes[crt]:
            if visit[i] == -1:
                dp[0][crt] += dp[1][i]
                dp[1][crt] += min(dp[0][i], dp[1][i])

print(min(dp[1][1], dp[0][1]))