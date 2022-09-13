from heapq import heappush, heappop
from sys import stdin


N, C = map(int, input().split())
minerals_dict = {i: [] for i in range(100001)}
for _ in range(N):
    X, Y, V = map(int, stdin.readline().split())
    minerals_dict[X].append((Y, V))

q = []
cur_value = 0
ans = 0
for x in range(100001):
    for y, value in minerals_dict[x]:
        heappush(q, (-1 * y, value))
        cur_value += value

    while len(q) > C:
        top_y, top_value = heappop(q)
        cur_value -= top_value
        while len(q) and top_y == q[0][0]:
            cur_value -= heappop(q)[1]

    ans = max(ans, cur_value)

print(ans)
