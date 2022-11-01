from itertools import combinations

l, c = map(int, input().split())
data = list(input().split())
pivot = ['a', 'e', 'i', 'o', 'u']
vowel, answer = [], []

for x in data:
    if x in pivot:
        vowel.append(x)

consonant = [i for i in data if i not in vowel]

tmp1, tmp2 = "", ""
for i in range(1, l - 1):
    for v in combinations(vowel, i):
        tmp1 += ''.join(list(v))
        vowel_cb = ''.join(list(v))
        for c in combinations(consonant, l - i):
            tmp1 += ''.join(list(c))
            tmp2 = ''.join(sorted(list(tmp1)))
            if tmp2 not in answer:
                answer.append(tmp2)
            tmp1 = vowel_cb
        tmp1 = ""

answer = sorted(list(set(answer)))
for x in answer:
    print(x)