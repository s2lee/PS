from collections import deque
import sys


def bfs():
    days = 0
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
    for x in graph:
        if 0 in x:
            return -1

    return days - 1


m, n = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

print(bfs())
