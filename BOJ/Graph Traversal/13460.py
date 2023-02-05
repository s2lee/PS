from collections import deque


def move(x, y, dx, dy):
    cnt = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            return -1
        for i in range(4):
            nrx, nry, cnt_r = move(rx, ry, dx[i], dy[i])
            nbx, nby, cnt_b = move(bx, by, dx[i], dy[i])
            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    return depth
                if nrx == nbx and nry == nby:
                    if cnt_r > cnt_b:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))

    return -1


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
queue = deque()
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

queue.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True
print(bfs())
