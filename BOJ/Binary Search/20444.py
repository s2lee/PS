n, k = map(int, input().split())


def solve():
    start, end = 0, n // 2
    while start <= end:
        mid = (start + end) // 2
        cnt = (mid + 1) * (n - mid + 1)
        if cnt == k:
            return "YES"

        if cnt < k:
            start = mid + 1
        else:
            end = mid - 1
    return "NO"


print(solve())
