import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleep = list(map(int, input().split()))
check = list(map(int, input().split()))

sleep_arr = [0] * (N+3)
check_arr = [1] * (N+3)

for s in sleep:
    sleep_arr[s] = 1

for c in check:
    if sleep_arr[c]:
        continue
    for num in range(c, N+3, c):
        if sleep_arr[num]:
            continue
        check_arr[num] = 0

dp = [0] * (N+3)
for i in range(3, N+3):
    dp[i] = dp[i-1] + check_arr[i]

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end] - dp[start-1])
