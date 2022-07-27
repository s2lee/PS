from collections import deque
import sys


def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        x, y, status = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][status]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][status] == 0:
                    visited[nx][ny][status] = visited[x][y][status] + 1
                    queue.append([nx, ny, status])

                if graph[nx][ny] == 1 and status == 0:
                    visited[nx][ny][status + 1] = visited[x][y][status] + 1
                    queue.append([nx, ny, status + 1])

    return -1


n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs())
