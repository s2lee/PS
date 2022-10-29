dp = [0] * 101
for i in range(1, 101):
    if i <= 3:
        dp[i] = 1
    else:
        dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    print(dp[int(input())])
