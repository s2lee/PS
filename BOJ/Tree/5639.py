import sys
from bisect import bisect
sys.setrecursionlimit(100000)


def solve(start, end):
    if start == end:
        return
    d = pre_order[start]
    idx = bisect(pre_order, d, start, end)
    solve(start + 1, idx)
    solve(idx, end)
    print(d)


pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

solve(0, len(pre_order))
