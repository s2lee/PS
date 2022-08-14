def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a != b:
        if a < b:
            parent[b] = a
            parent_cnt[a] += parent_cnt[b]
            parent_cnt[b] = 0
        else:
            parent[a] = b
            parent_cnt[b] += parent_cnt[a]
            parent_cnt[a] = 0


N = int(input())
parent = [x for x in range(1000001)]
parent_cnt = [1 for x in range(1000001)]
for _ in range(N):
    temp = list(input().split())
    if temp[0] == "I":
        union_parent(int(temp[1]), int(temp[2]))
    else:
        c = find_parent(int(temp[1]))
        print(parent_cnt[c])
