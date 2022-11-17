n, w = map(int, input().split())
graph = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] += 1

num_leaf = 0
for i in range(2, n + 1):
    if graph[i] == 1:
        num_leaf += 1

print(round(w / num_leaf, 10))
