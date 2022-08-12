def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if friends_cost[x] < friends_cost[y]:
        parent[y] = x
    else:
        parent[x] = y


N, M, k = map(int, input().split())
parent = [i for i in range(N + 1)]
friends_cost = [0] + list(map(int, input().split()))
for _ in range(M):
    v, w = map(int, input().split())
    union_parent(v, w)

friends = set()
answer = 0
for i in range(1, N + 1):
    idx = find_parent(i)
    if idx not in friends:
        friends.add(idx)
        answer += friends_cost[idx]
print(answer if answer <= k else "Oh no")
