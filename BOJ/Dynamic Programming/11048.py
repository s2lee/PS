import sys

n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = array[:]
for i in range(n):
    for j in range(m):
        down_side = dp[i - 1][j]
        right_side = dp[i][j - 1]
        dia_side = dp[i - 1][j - 1]
        if i == 0:
            dia_side, down_side = 0, 0
        if j == 0:
            dia_side, right_side = 0, 0
        dp[i][j] += max(down_side, right_side, dia_side)

print(dp[n - 1][m - 1])
