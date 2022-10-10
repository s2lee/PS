import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
sum_value = array[0]
result = array[0]
for i in range(1, n):
    sum_value += array[i]
    if sum_value < 0:
        sum_value = min(result, 0)
    result = max(result, sum_value)

print(max(result, max(array)))