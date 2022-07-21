def watch(x, y, direction):
    ret = set()
    for d in direction:
        nx, ny = x, y
        while 1:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break

            if office[nx][ny] == 6:
                break

            if office[nx][ny] == 0:
                ret.add((nx, ny))

    return ret


def dfs(n, watched_set):
    global max_watched_cnt

    if n == len(cctv):
        max_watched_cnt = max(max_watched_cnt, len(watched_set))
        return

    for cctv_cases in cctv[n]:
        dfs(n + 1, watched_set | cctv_cases)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
cctv, blank, max_watched_cnt = [], 0, 0
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            blank += 1
        elif office[i][j] == 1:
            cctv.append([watch(i, j, [k]) for k in range(4)])
        elif office[i][j] == 2:
            cctv.append([watch(i, j, [k, k + 2]) for k in range(2)])
        elif office[i][j] == 3:
            cctv.append([watch(i, j, [k, (k + 1) % 4]) for k in range(4)])
        elif office[i][j] == 4:
            cctv.append([watch(i, j, [k, (k + 1) % 4, (k + 2) % 4]) for k in range(4)])
        elif office[i][j] == 5:
            cctv.append([watch(i, j, [0, 1, 2, 3])])

dfs(0, set())
print(blank - max_watched_cnt)
