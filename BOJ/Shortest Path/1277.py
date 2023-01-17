from heapq import heappush, heappop
from math import inf, sqrt
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
M = float(input())

power_plant = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    power_plant[i] = list(map(int, input().split()))

connected = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(W):
    a, b = map(int, input().split())
    connected[a][b] = 1
    connected[b][a] = 1

hq = []
heappush(hq, [0, 1])
wire_length = [inf for _ in range(N + 1)]
wire_length[1] = 0
while hq:
    cur_length, cur_plant = heappop(hq)
    for next_plant in range(1, N + 1):
        if connected[cur_plant][next_plant] and cur_length < wire_length[next_plant]:
            wire_length[next_plant] = cur_length
            heappush(hq, [cur_length, next_plant])
        else:
            x1, y1 = power_plant[cur_plant][0], power_plant[cur_plant][1]
            x2, y2 = power_plant[next_plant][0], power_plant[next_plant][1]
            length = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
            if length <= M:
                total_length = cur_length + length
                if total_length < wire_length[next_plant]:
                    wire_length[next_plant] = total_length
                    heappush(hq, [total_length, next_plant])

print(int(wire_length[N] * 1000))
