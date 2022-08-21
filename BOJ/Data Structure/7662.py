import sys
import heapq


def item_pop(q, visited):
    while q and not visited[q[0][1]]:
        heapq.heappop(q)


case_num = int(input())
for _ in range(case_num):
    max_heap, min_heap = [], []
    visited = [False] * 1000000

    order_num = int(input())
    for key in range(order_num):
        order = sys.stdin.readline().split()
        if order[0] == "I":
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (-int(order[1]), key))
            visited[key] = True
        elif order[0] == "D":
            if order[1] == "1":
                item_pop(max_heap, visited)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif order[1] == "-1":
                item_pop(min_heap, visited)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    item_pop(max_heap, visited)
    item_pop(min_heap, visited)

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
