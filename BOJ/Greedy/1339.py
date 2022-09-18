n = int(input())
array = [input().rstrip() for _ in range(n)]
alpha = [0] * 26
for s in array:
    for i in range(len(s)):
        alpha[ord(s[i]) - ord('A')] += 10 ** (len(s) - i - 1)

alpha.sort(reverse=True)

ans = 0
for i in range(9, -1, -1):
    ans += alpha[9 - i] * i

print(ans)
