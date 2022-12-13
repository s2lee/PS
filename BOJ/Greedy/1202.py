import sys
import heapq
input = sys.stdin.readline


def sol(N, K, jewel, bags):
    jewel.sort(key=lambda x: -x[0])
    bags.sort(reverse=True)
    stolen = []
    for weight, price in jewel:
        stolen_count = len(stolen)
        if stolen_count >= K or weight > bags[stolen_count]:
            if stolen_count == 0:
                continue
            heapq.heappush(stolen, price)
            heapq.heappop(stolen)
        else:
            heapq.heappush(stolen, price)

    print(sum(stolen))


N, K = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input().rstrip()) for _ in range(K)]
sol(N, K, jewel, bags)