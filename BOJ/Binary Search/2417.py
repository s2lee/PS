n = int(input())


def binary_search(n):
    if n == 1:
        return 1

    start = 0
    end = n - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid >= n:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    return ans


print(binary_search(n))
