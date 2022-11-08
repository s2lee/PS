for _ in range(int(input())):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        px, py, pr = map(int, input().split())
        d1 = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
        d2 = (((x2 - px) ** 2) + ((y2 - py) ** 2)) ** 0.5
        if d1 < pr < d2 or d2 < pr < d1:
            cnt += 1
    print(cnt)
