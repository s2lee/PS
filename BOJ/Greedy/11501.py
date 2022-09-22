import sys

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    max_profit = 0
    max_value = data[-1]

    for i in range(n - 2, -1, -1):
        if data[i] <= max_value:
            max_profit += (max_value - data[i])
        else:
            max_value = data[i]

    print(max_profit)
