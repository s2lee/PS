import sys

n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
cnt = [0] * 100001
ans = 1
left, right = 0, 1
cnt[array[0]] += 1

while right < n:
    if cnt[array[right]] < k:
        cnt[array[right]] += 1
        right += 1
        ans = max(ans, right - left)
    else:
        cnt[array[left]] -= 1
        left += 1

print(ans)
