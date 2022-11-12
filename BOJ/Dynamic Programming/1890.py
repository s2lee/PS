import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        num = board[i][j]
        if num == 0:
            continue
        if 0 <= j + num < n:
            dp[i][j + num] += dp[i][j]
        if 0 <= i + num < n:
            dp[i + num][j] += dp[i][j]

print(dp[-1][-1])
