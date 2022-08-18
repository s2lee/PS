from collections import deque


N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(1, temp[0]):
        graph[temp[i]].append(temp[i + 1])
        in_degree[temp[i + 1]] += 1

result = []
q = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

if len(result) == N:
    for element in result:
        print(element)
else:
    print(0)
