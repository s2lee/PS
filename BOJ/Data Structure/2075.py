import heapq, sys


n = int(input())
h = []
for _ in range(n):
    for num in map(int, sys.stdin.readline().split()):
        if h:
            if h[0] < num:
                heapq.heappush(h, num)
                if len(h) > n:
                   heapq.heappop(h)
        else:
            heapq.heappush(h, num)

print(heapq.heappop(h))
