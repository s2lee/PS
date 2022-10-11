import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

sum_value = 0
min_price = sys.maxsize
for i in range(len(length)):
    if price[i] < min_price:
        sum_value += price[i] * length[i]
        min_price = price[i]
    else:
        sum_value += min_price * length[i]

print(sum_value)
