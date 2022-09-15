import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())

titles, scores = [], []
for i in range(n):
    title, score = input().split()
    titles.append(title)
    scores.append(int(score))

query_list = []
for _ in range(m):
    query_list.append(int(input()))

for query in query_list:
    print(titles[bisect.bisect_left(scores, query)])
