import sys

i = 0
while True:
    i += 1
    l, p, v = map(int, sys.stdin.readline().split())
    if l == p == v == 0:
        break
    tmp = v // p * l
    tmp += min(l, v % p)
    print(f'Case {i}: {tmp}')