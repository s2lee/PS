import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
count = [0] * (d + 1)
count[c] += 1
nodes = [int(input()) for _ in range(N)]

idx = 0
idx2 = k - 1
kind = 1
for i in range(k):
    count[nodes[i]] += 1
    if count[nodes[i]] == 1:
        kind += 1
ans = -1

while idx < N:
    idx += 1
    count[nodes[idx - 1]] -= 1
    if count[nodes[idx - 1]] == 0:
        kind -= 1

    idx2 += 1
    if idx2 >= N:
        idx2 -= N

    count[nodes[idx2]] += 1
    if count[nodes[idx2]] == 1:
        kind += 1

    ans = max(kind, ans)

print(ans)
