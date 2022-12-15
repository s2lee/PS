import sys
input = sys.stdin.readline


def solve():
    now = 301
    ans = 0
    while now < 1201:
        _next = now
        for x in arr:
            if _next <= x[1] and x[0] <= now:
                _next = x[1]
        if _next == now:
            print(0)
            return
        ans += 1
        now = _next

    print(ans)


n = int(input())
arr = [[0, 0] for _ in range(n)]
for i in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    arr[i][0], arr[i][1] = m1 * 100 + d1, m2 * 100 + d2

solve()
