N, M, L = map(int, input().split())
rest = [0] + sorted(list(map(int, input().split()))) + [L]
left, right = 1, L
res = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, N + 2):
        cnt += (rest[i] - rest[i - 1] - 1) // mid

    if cnt <= M:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
