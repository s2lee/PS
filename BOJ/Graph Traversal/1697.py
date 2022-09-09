from collections import deque


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v == k:
            return time[v]
        for next_step in (v - 1, v + 1, v * 2):
            if 0 <= next_step < 100001 and not time[next_step]:
                time[next_step] = time[v] + 1
                queue.append(next_step)


n, k = map(int, input().split())
time = [0] * 100001
print(bfs())
