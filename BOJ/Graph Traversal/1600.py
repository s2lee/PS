from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
check = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hx = [-2, -2, -1, 1, 2, 2, -1, 1]
hy = [-1, 1, -2, -2, -1, 1, 2, 2]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    while q:
        x, y, z = q.popleft()

        if x == (H - 1) and y == (W - 1):
            return check[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and not check[nx][ny][z] and not grid[nx][ny]:
                check[nx][ny][z] = check[x][y][z] + 1
                q.append([nx, ny, z])

        if z == K:
            continue

        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]

            if 0 <= nx < H and 0 <= ny < W and not check[nx][ny][z + 1] and not grid[nx][ny]:
                check[nx][ny][z + 1] = check[x][y][z] + 1
                q.append([nx, ny, z + 1])
    return -1


print(bfs())
