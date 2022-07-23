import sys


def dfs(now_city, total_cost):
    global answer

    if total_cost >= answer:
        return

    if sum(visited) == n - 1:
        if cost[now_city][0]:
            answer = min(answer, total_cost + cost[now_city][0])
        return

    for next_city in range(1, n):
        if cost[now_city][next_city] and not visited[next_city]:
            visited[next_city] = 1
            dfs(next_city, total_cost + cost[now_city][next_city])
            visited[next_city] = 0


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
answer = sys.maxsize
for i in range(1, n):
    if cost[0][i]:
        visited[i] = 1
        dfs(i, cost[0][i])
        visited[i] = 0

print(answer)
