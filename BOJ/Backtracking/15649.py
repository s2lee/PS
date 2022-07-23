n, m = map(int, input().split())
visited = [False] * n
result = []


def solve(count):
    if count == m:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            solve(count + 1)
            visited[i] = False
            result.pop()


solve(0)
