import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 1 <= nx < n - 1 and 1 <= ny < m - 1:
            if ice[nx][ny] > 0 and not visited[nx][ny]:
                dfs(nx, ny)


def melt():
    ice_copy = [item[:] for item in ice]
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if ice_copy[x][y] > 0:
                sub_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if ice_copy[nx][ny] == 0:
                        sub_count += 1
                ice[x][y] = max(ice_copy[x][y] - sub_count, 0)


n, m = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

    check, ice_count = False, 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ice[i][j] > 0 and not visited[i][j]:
                dfs(i, j)
                ice_count += 1
                if ice_count == 2:
                    check = True
                    break
    if check:
        break

    if ice_count == 0:
        year = 0
        break

    melt()
    year += 1

print(year)
