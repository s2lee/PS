import sys


def dfs(stu_cnt, y_count):
    if y_count > 3:
        return

    if stu_cnt == 7:
        answer.add(tuple(sorted(stack)))
        return

    can = set()
    for sx, sy in stack:
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                can.add((nx, ny))

    for cx, cy in can:
        visited[cx][cy] = True
        stack.append((cx, cy))
        if graph[cx][cy] == 'S':
            dfs(stu_cnt + 1, y_count)
        else:
            dfs(stu_cnt + 1, y_count + 1)
        visited[cx][cy] = False
        stack.pop()


graph = [sys.stdin.readline().rstrip() for _ in range(5)]
s_list = []
for i in range(5):
    for j in range(5):
        if graph[i][j] == 'S':
            s_list.append([i, j])

answer = set()
stack = []
visited = [[False] * 5 for _ in range(5)]
for x, y in s_list:
    visited[x][y] = True
    stack.append((x, y))
    dfs(1, 0)
    stack.pop()

print(len(answer))
