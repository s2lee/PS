n, a, b = map(int, input().split())
num_round = 0
while a != b:
    a -= a // 2
    b -= b // 2
    num_round += 1

print(num_round)
