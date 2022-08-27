import sys


n = int(input())
array = sorted(list(map(int, input().rsplit())))
left, right = 0, n - 1
lowest = sys.maxsize
low_l, low_r = 0, 0

while left < right:
    sum_value = array[left] + array[right]
    if abs(sum_value) < lowest:
        lowest = abs(sum_value)
        low_l, low_r = array[left], array[right]

    if sum_value >= 0:
        right -= 1
    else:
        left += 1

print(low_l, low_r)
