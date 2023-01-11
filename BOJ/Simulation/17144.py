import sys
input = sys.stdin.readline


def spread_dust() -> list:
    new_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if array[i][j] > 0:
                amount = array[i][j] // 5
                cnt = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_i, next_j = i + dx, j + dy
                    if 0 <= next_i < r and 0 <= next_j < c and not array[next_i][next_j] == -1:
                        new_arr[next_i][next_j] += amount
                        cnt += 1
                new_arr[i][j] += array[i][j] - amount * cnt

    new_arr[p][0], new_arr[q][0] = -1, -1
    return new_arr


r, c, t = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(r)]
p, q = 0, 0
for idx in range(r):
    if array[idx][0] == -1:
        p, q = idx, idx + 1
        break

for _ in range(t):
    array = spread_dust()

    for i in range(p - 1, 0, -1):
        array[i][0] = array[i - 1][0]

    for i in range(c - 1):
        array[0][i] = array[0][i + 1]

    for i in range(p):
        array[i][c - 1] = array[i + 1][c - 1]

    for i in range(c - 1, 1, -1):
        array[p][i] = array[p][i - 1]

    array[p][1] = 0

    for j in range(q + 1, r - 1):
        array[j][0] = array[j + 1][0]

    for j in range(c - 1):
        array[r - 1][j] = array[r - 1][j + 1]

    for j in range(r - 1, q, -1):
        array[j][c - 1] = array[j - 1][c - 1]

    for j in range(c - 1, 1, -1):
        array[q][j] = array[q][j - 1]

    array[q][1] = 0

ans = sum(sum(x) for x in array)
print(ans + 2)
