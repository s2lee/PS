from collections import defaultdict
import sys

input = sys.stdin.readline


n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
result = [[5] * n for _ in range(n)]
tree = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[(x - 1, y - 1)].append(z)

for _ in range(k):
    for key in tree.keys():
        r, c = key
        tree[key].sort()
        aged_tree = []
        dead_amount = 0
        for v in tree[key]:
            if result[r][c] >= v:
                result[r][c] -= v
                aged_tree.append(v + 1)
            else:
                dead_amount += (v // 2)

        result[r][c] += dead_amount
        tree[key] = aged_tree

    temp_tree = tree.copy()
    for key in temp_tree.keys():
        r, c = key
        for v in temp_tree[key]:
            if v % 5 == 0:
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, - 1), (1, 0), (1, 1)]:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < n and 0 <= next_c < n:
                        tree[(next_r, next_c)].append(1)

    for i in range(n):
        for j in range(n):
            result[i][j] += array[i][j]

ans = sum(len(x) for x in tree.values())
print(ans)
