n = int(input())
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
visited = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    visited[x][y] = 1

    dir_idx = [d]
    for _ in range(g):
        dir_idx += list(map(lambda x: (x + 1) % 4, reversed(dir_idx)))

    for i in dir_idx:
        dx, dy = direction[i]
        x, y = x + dx, y + dy
        visited[x][y] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if (
            visited[i][j]
            and visited[i + 1][j]
            and visited[i][j + 1]
            and visited[i + 1][j + 1]
        ):
            ans += 1

print(ans)
