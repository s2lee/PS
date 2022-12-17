s1 = input()
s2 = input()

dp = [0]*len(s2)
for i in range(len(s1)):
    s = s1[i]
    cnt = 0
    for j in range(len(s2)):
        if dp[j] > cnt:
            cnt = dp[j]
        elif s == s2[j]:
            dp[j] = cnt + 1

print(max(dp))
