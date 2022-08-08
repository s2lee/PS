k, n = map(int, input().split())
lan_line = [int(input()) for _ in range(k)]
start, end = 1, sum(lan_line) // n
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum([x // mid for x in lan_line])
    if cnt >= n:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
