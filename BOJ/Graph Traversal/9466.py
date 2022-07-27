import sys
sys.setrecursionlimit(111111)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    choice = graph[x]

    if visited[choice]:
        if choice in cycle:
            result += cycle[cycle.index(choice):]
        return
    else:
        dfs(choice)


for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))
