import sys
from collections import deque

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    array.sort(reverse=True)
    ans = deque()
    ans.append(array[0])
    array = array[1:]
    for i in range(n - 1):
        if i % 2 == 0:
            ans.append(array[i])
        else:
            ans.appendleft(array[i])

    result = []
    while ans:
        x = ans.popleft()
        result.append(x)

    max_value = 0
    for i in range(n - 1):
        max_value = max(max_value, abs(result[i] - result[i + 1]))

    print(max_value)
