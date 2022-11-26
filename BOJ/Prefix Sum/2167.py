from itertools import accumulate
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
acc = [[0] * (m + 1)]
for i in range(1, n + 1):
    row = accumulate(map(int, input().split()), initial=0)
    acc.append([acc[-1][j] + r for j, r in enumerate(row)])

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(acc[x][y] - acc[x][j - 1] - acc[i - 1][y] + acc[i - 1][j - 1])