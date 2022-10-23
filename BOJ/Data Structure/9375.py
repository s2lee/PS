import sys


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    fashion = {}
    n = int(input())
    for _ in range(n):
        name_costume, type_costume = input().split()
        if type_costume in fashion.keys():
            fashion[type_costume].append(name_costume)
        else:
            fashion[type_costume] = [name_costume]

    for key, value in fashion.items():
        fashion[key].append('')

    res = 1
    for value in fashion.values():
        res *= len(value)

    print(res - 1)
