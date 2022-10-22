from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((i, array[i]))

    cnt = 1
    while q:
        x = q.popleft()
        check = False
        for y in q:
            if x[1] < y[1]:
                q.append(x)
                check = True
                break

        if check:
            continue
        else:
            if x[0] == m:
                print(cnt)
            else:
                cnt += 1