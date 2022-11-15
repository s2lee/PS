n = int(input())
graph = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if graph[k] > 1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
