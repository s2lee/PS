def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y
    else:
        return


n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
for i in range(1, n + 1):
    cities = list(map(int, input().split()))
    for j in range(1, n + 1):
        if cities[j - 1] == 1:
            union_parent(i, j)

plan = list(map(int, input().split()))
res = set([find_parent(i) for i in plan])
print("YES" if len(res) == 1 else "NO")
