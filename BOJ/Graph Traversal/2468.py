import sys
sys.setrecursionlimit(100000)


n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
array = [[0] * n for _ in range(n)]


def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False

    if array[x][y] == 0:
        array[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


max_value = 1
for height in range(1, 101):
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                array[i][j] = 2

    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                count += 1
    max_value = max(count, max_value)

    for i in range(n):
        for j in range(n):
            array[i][j] = 0

print(max_value)
