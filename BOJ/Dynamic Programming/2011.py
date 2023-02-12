n = list(input().strip())

dp = [0 for _ in range(len(n) + 1)]
dp[0], dp[1] = 1, 1

if n[0] == "0":
    print(0)
else:
    for i in range(2, len(n) + 1):
        if int(n[i - 1]) > 0:
            dp[i] += dp[i - 1]
        num = int(n[i - 1]) + int(n[i - 2]) * 10
        if 10 <= num <= 26:
            dp[i] += dp[i - 2]
    print(dp[len(n)] % 1000000)
