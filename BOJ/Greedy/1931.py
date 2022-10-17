import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    array.append((s, e))

array.sort(key=lambda x: (x[1], x[0]))
cnt, end = 0, 0
for s, e in array:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
