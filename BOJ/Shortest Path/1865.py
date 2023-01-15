def bellman_ford():
    dist = [10001] * (n + 1)
    dist[1] = 0
    for cnt in range(n):
        for start, end, time in graph:
            if dist[end] > dist[start] + time:
                if cnt == n - 1:
                    return True
                dist[end] = dist[start] + time
    return False


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    print("YES" if bellman_ford() else "NO")