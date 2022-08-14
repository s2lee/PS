def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = x
        network[x] += network[y]
    return network[x]


for _ in range(int(input())):
    parent = dict()
    network = dict()
    for _ in range(int(input())):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            network[a] = 1
        if b not in parent:
            parent[b] = b
            network[b] = 1

        print(union_parent(a, b))
