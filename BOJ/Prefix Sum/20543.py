import sys

N, M = map(int, input().split())
K = M // 2
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

result = [[0 for _ in range(N)] for _ in range(N)]
prefix_sum = [[0 for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        if x + K >= N or y + K >= N:
            continue
        right_x, right_y = x + K, y + K
        left_x, left_y = max(x - K, 1), max(y - K, 1)
        prefix_sum[right_x][right_y] = (prefix_sum[right_x - 1][right_y] +
                                        prefix_sum[right_x][right_y - 1] -
                                        prefix_sum[right_x - 1][right_y - 1] +
                                        result[right_x][right_y])
        prev_bomb = (prefix_sum[right_x][right_y] -
                     prefix_sum[left_x - 1][right_y] -
                     prefix_sum[right_x][left_y - 1] +
                     prefix_sum[left_x - 1][left_y - 1])
        result[right_x][right_y] = -arr[x][y] - prev_bomb
        prefix_sum[right_x][right_y] += result[right_x][right_y]

for row in result:
    print(*row)
