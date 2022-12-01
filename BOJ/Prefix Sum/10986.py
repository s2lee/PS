n, m = map(int, input().split())
array = list(map(int, input().split()))

cnt = [0] * m
cnt[0] = 1
prefix_sum = 0
for num in array:
    prefix_sum += num
    cnt[prefix_sum % m] += 1

ans = 0
for i in range(m):
    ans += (cnt[i] * (cnt[i] - 1) // 2)

print(ans)
