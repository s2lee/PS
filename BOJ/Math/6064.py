for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    k = -1
    check = False
    while x <= m * n:
        if (x - y) % n == 0:
            k = x
            check = True
            break
        x += m

    print(k if check else -1)
