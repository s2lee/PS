from itertools import combinations
import sys

n = int(input())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize

for members in combinations(range(n), n // 2):
    start = members
    link = list(set(range(n)) - set(start))
    start_ability, link_ability = 0, 0

    for x, y in combinations(start, 2):
        start_ability += s[x][y] + s[y][x]

    for x, y in combinations(link, 2):
        link_ability += s[x][y] + s[y][x]

    answer = min(answer, abs(link_ability - start_ability))

print(answer)
