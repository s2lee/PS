import sys

p = sys.stdin.readline().strip().replace('()', 'l')

res, cnt = 0, 0
for x in p:
    if x == '(':
        cnt += 1
    elif x == 'l':
        res += cnt
    else:
        res += 1
        cnt -= 1

print(res)
