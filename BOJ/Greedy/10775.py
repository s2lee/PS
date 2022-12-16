import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
answer = 0
for _ in range(P):
    g = int(input())
    docking = find_parent(g)
    if docking == 0:
        break
    parent[docking] = parent[docking - 1]
    answer += 1

print(answer)