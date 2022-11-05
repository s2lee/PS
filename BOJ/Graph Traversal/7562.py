from collections import deque


def bfs():
    queue = deque()
    queue.append((cur_x, cur_y))
    while queue:
        x, y = queue.popleft()
        if x == move_x and y == move_y:
            return graph[move_x][move_y]
        for dx, dy in step:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for _ in range(int(input())):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    move_x, move_y = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    step = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2)]
    print(bfs())
