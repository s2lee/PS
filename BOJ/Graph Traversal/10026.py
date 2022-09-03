import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if graph[nx][ny] == color:
                    dfs(nx, ny)


n = int(input())
graph = [list(sys.stdin.readline()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt, rgb_cnt = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            rgb_cnt += 1

print(cnt, rgb_cnt)
