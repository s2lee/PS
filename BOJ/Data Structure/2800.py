from itertools import combinations


exp = [*input().strip()]

temp, idx_bracket = [], []
for i, p in enumerate(exp):
    if p == '(':
        exp[i] = ''
        temp += [i]
    if p == ')':
        exp[i] = ''
        idx_bracket += [[temp.pop(), i]]

result = set()
for n in range(len(idx_bracket)):
    for cb in combinations(idx_bracket, n):
        P = exp[:]
        for i, j in cb:
            P[i] = '('
            P[j] = ')'

        result.add(''.join(P))

for r in sorted(result):
    print(r)
