import sys

n = int(input())
array = [0]
for _ in range(n):
    array.append(int(sys.stdin.readline()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        dp[i] = array[1]
    elif i == 2:
        dp[i] = array[1] + array[2]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i])

print(dp[n])