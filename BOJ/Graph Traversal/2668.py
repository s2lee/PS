def dfs(node, start):
    visited[node] = True
    next_num = num[node]
    if not visited[next_num]:
        dfs(next_num, start)
    elif visited[next_num] and next_num == start:
        result.append(next_num)


n = int(input())
num = [0] + [int(input()) for _ in range(n)]
result = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(result))
for x in result:
    print(x)
