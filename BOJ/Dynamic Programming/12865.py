import sys
input = sys.stdin.readline


N, K = map(int, input().rstrip().split())
stuff = []

for _ in range(N):
    w, v = map(int, input().rstrip().split())
    stuff.append((w, v))

stuff.sort()

dp = [0] * (K + 1)

for w, v in stuff:
    for x in range(K, w - 1, -1):
        dp[x] = max(dp[x - w] + v, dp[x])

print(dp[-1])
