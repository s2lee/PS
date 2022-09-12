import sys

n = int(input())
h = list(map(int, sys.stdin.readline().split()))

stack = []
answer = [0 for _ in range(n)]
for i in range(len(h)):
    while stack:
        if stack[-1][1] > h[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append([i, h[i]])

print(*answer)
