from itertools import combinations

n, m = map(int, input().split())
data, house, chicken = [], [], []

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i, j))

        if data[i][j] == 1:
            house.append((i, j))

candidates = list(combinations(chicken, m))


def get_sum_distance(x):
    sum_value = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in x:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        sum_value += temp
    return sum_value


result = 1e9
for candidate in candidates:
    result = min(result, get_sum_distance(candidate))

print(result)
