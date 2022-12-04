import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [0] * (n + 1)
cnt = 0
for i in range(n - 1):
    if data[i] > data[i + 1]:
        cnt += 1
    dp[i + 1] = cnt

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(dp[y - 1] - dp[x - 1])