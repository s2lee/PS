from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = -visited[node]
            else:
                if visited[i] == visited[node]:
                    return False
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    flag = True
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break

    print('YES' if flag else 'NO')
