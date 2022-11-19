for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a

    node1, node2 = map(int, input().split())
    result = set()
    while parent[node1] != node1:
        result.add(node1)
        node1 = parent[node1]

    while node2 not in result:
        node2 = parent[node2]

    print(node2)
