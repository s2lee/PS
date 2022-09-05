from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = {(x, y)}
    while q:
        x, y = q.popleft()
        if abs(x - end_x) + abs(y - end_y) <= 1000:
            return "happy"

        for nx, ny in store:
            dist = abs(x - nx) + abs(y - ny)
            if dist <= 1000 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))

    return "sad"


for _ in range(int(input())):
    n = int(input())
    house_x, house_y = map(int, input().split())
    store = [tuple(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int, input().split())

    print(bfs(house_x, house_y))
