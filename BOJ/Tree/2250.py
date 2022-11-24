import sys


def dfs(num, depth):
    global cnt
    if num == -1:
        return
    if depth not in res:
        res[depth] = [9876543210, -9876543210]
    dfs(tr[num][0], depth + 1)
    res[depth][0] = min(res[depth][0], cnt)
    res[depth][1] = max(res[depth][1], cnt)
    cnt += 1
    dfs(tr[num][1], depth + 1)


n = int(sys.stdin.readline())
tr = [[-1] * 2 for _ in range(n + 1)]
res = dict()
cnt = 1
ind = [0] * (n + 1)

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if b != -1:
        tr[a][0] = bbm
        ind[b] += 1
    if c != -1:
        tr[a][1] = c
        ind[c] += 1

root = -1
for i in range(1, n + 1):
    if not ind[i]:
        root = i

dfs(root, 1)
ans = []
for i in res:
    ans.append((res[i][1] - res[i][0] + 1, i))

ans.sort(key=lambda x: (-x[0], x[1]))
print(ans[0][1], ans[0][0])

