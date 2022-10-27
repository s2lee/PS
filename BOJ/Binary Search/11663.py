import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
point = sorted(list(map(int, input().split())))

for _ in range(m):
    start, end = map(int, input().split())
    print(bisect_right(point, end) - bisect_left(point, start))
