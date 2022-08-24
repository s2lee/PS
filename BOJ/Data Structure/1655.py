import heapq

n = int(input())
max_h, min_h = [], []
for i in range(n):
    num = int(input())

    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if min_h and -max_h[0] > min_h[0]:
        heapq.heappush(max_h, -heapq.heappop(min_h))
        heapq.heappush(min_h, -heapq.heappop(max_h))

    print(-max_h[0])
