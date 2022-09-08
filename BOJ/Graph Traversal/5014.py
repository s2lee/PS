from collections import deque


def bfs():
    q = deque()
    q.append((S, 0))
    visited[S] = True
    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt

        for x in [U, -D]:
            next_x = now + x
            if 0 < next_x <= F:
                if not visited[next_x]:
                    visited[next_x] = True
                    q.append((next_x, cnt + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)
print(bfs())
