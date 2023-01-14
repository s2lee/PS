import sys
import heapq

INF = sys.maxsize
n, k = map(int, input().split())
dp = [INF] * 100001


def dijkstra(n, k):
    if k <= n:
        print(n - 1)
        return

    q = []
    heapq.heappush(q, (0, n))
    while q:
        time, now = heapq.heappop(q)
        for next_step in now - 1, now + 1, now * 2:
            if 0 <= next_step < 100001 and dp[next_step] == INF:
                if next_step == now * 2:
                    dp[next_step] = time
                    heapq.heappush(q, (time, 2 * now))

                else:
                    dp[next_step] = time + 1
                    heapq.heappush(q, (time + 1, next_step))
    print(dp[k])


dijkstra(n, k)
