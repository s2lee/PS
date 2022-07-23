from itertools import permutations

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

n = int(input())
removed_cnt = 0
for _ in range(n):
    n, s, b = map(int, input().split())
    n = list(str(n))
    removed_cnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= removed_cnt
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            removed_cnt += 1

print(len(num))
