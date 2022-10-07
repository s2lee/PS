import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    global area
    if x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 2
            area += 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
    return False


m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
array = []
for _ in range(k):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(k):
    for x in range(m - array[i][3], m - array[i][1]):
        for y in range(array[i][0], array[i][2]):
            graph[x][y] = 1

count, area = 0, 0
result = []
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            count += 1
            result.append(area)
            area = 0

print(count)
result.sort()
for x in result:
    print(x, end=' ')

