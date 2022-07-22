board = ('WB' * 4 + 'BW' * 4) * 4
ans = 9999
n, m = map(int, input().split())
s = [input() for _ in range(n)]

for i in range(n - 7):
    for j in range(m - 7):
        tmp = ''.join([line[j:j+8] for line in s[i:i+8]])
        p = sum(x != y for x, y in zip(board, tmp))
        ans = min(ans, p, 64 - p)

print(ans)
