import sys

n = int(sys.stdin.readline())
array = list(range(n, 0, -1))
ans = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
temp = ''
i = 0
res = []
while array:
    k = ans[i]
    if len(stack) != 0:
        if k == stack[-1]:
            res.append(stack.pop())
            temp += '-'
            i += 1
            continue

    for _ in range(k - array[-1] + 1):
        stack.append(array.pop())
        temp += '+'

    res.append(stack.pop())
    temp += '-'
    i += 1

if ans == res + stack[::-1]:
    temp += '-' * len(stack)
    for x in temp:
        print(x)
else:
    print("NO")
