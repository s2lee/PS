from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())
array = [list(stdin.readline().strip()) for _ in range(r)]
dist = [[0] * c for _ in range(r)]
q = deque()
for i in range(r):
    for j in range(c):
        if array[i][j] == 'J':
            px, py = i, j
        elif array[i][j] == 'F':
            q.append((i, j, 1))
            dist[i][j] = 1


def bfs():
    q.append((px, py, 0))
    dist[px][py] = 1
    while q:
        x, y, f = q.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                if f:
                    continue
                print(dist[x][y])
                return

            if not dist[nx][ny] and array[nx][ny] != '#':
                q.append((nx, ny, f))
                dist[nx][ny] = dist[x][y] + 1
    print("IMPOSSIBLE")


bfs()
