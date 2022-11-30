n, k = map(int, input().split())
array = list(map(int, input().split()))
ans, prefix_sum, cnt = 0, 0, {0: 1}
for i in range(n):
    prefix_sum += array[i]
    if prefix_sum - k in cnt:
        ans += cnt[prefix_sum - k]
    if prefix_sum in cnt:
        cnt[prefix_sum] += 1
    else:
        cnt[prefix_sum] = 1

print(ans)
