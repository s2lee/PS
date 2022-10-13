import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    array = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append((x, y))
    array.sort(key=lambda x:x[0])

    cnt, tmp = 0, 100001
    for x, y in array:
        if y < tmp:
            cnt += 1
        tmp = min(tmp, y)

    print(cnt)
