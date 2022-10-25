N = int(input())
array = sorted(list(map(int, input().split())))
M = int(input())


def solution(data, n, m):
    if sum(data) <= m:
        return max(data)

    start = 0
    end = data[n - 1]
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in data:
            if i < mid:
                temp += i
            else:
                temp += mid

        if temp > m:
            end = mid - 1
        else:
            start = mid + 1
            ans = max(ans, mid)

    return ans


print(solution(array, N, M))
