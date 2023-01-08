from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
cmd = [tuple(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
q = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for d, s in cmd:
    moved_cloud = []
    while q:
        x, y = q.popleft()
        nx, ny = (x + dx[d - 1] * s) % n, (y + dy[d - 1] * s) % n
        array[nx][ny] += 1
        moved_cloud.append((nx, ny))

    for x, y in moved_cloud:
        for i in range(1, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny]:
                array[x][y] += 1

    for i in range(n):
        for j in range(n):
            if (i, j) not in moved_cloud and array[i][j] >= 2:
                q.append((i, j))
                array[i][j] -= 2

ans = sum(sum(array[i]) for i in range(n))
print(ans)
