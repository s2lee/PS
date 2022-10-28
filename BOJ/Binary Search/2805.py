n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

start = 0
end = data[n - 1]
res = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in data:
        if i > mid:
            temp += i - mid

    if temp >= m:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)
