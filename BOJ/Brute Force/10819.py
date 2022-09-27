from itertools import permutations


n = int(input())
data = list(map(int, input().split()))

result = 0
for pm in permutations(data, n):
    sum_value = 0
    for i in range(n - 1):
        sum_value += abs(pm[i] - pm[i + 1])
    result = max(result, sum_value)

print(result)
