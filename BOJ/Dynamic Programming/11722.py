import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if array[j] > array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))