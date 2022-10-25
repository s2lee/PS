import sys


n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

res = 1e9
left, right = 0, 1
sum_value = data[left]
while left < right:
    if sum_value >= s:
        res = min(res, right - left)
        sum_value -= data[left]
        left += 1
    elif sum_value < s:
        if right <= n - 1:
            sum_value += data[right]
            right += 1
        else:
            break

if res == 1e9:
    print(0)
else:
    print(res)
