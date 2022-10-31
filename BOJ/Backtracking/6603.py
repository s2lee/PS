import sys


def solve(cnt, idx):
    if cnt == 6:
        print(" ".join(map(str, result)))
        return

    for i in range(idx, k):
        if not visited[i]:
            visited[i] = True
            result.append(s[i])
            solve(cnt + 1, i)
            visited[i] = False
            result.pop()


while True:
    array = list(map(int, sys.stdin.readline().split()))
    k = array[0]
    s = array[1:]
    result = []
    visited = [False] * k
    if k == 0:
        break

    solve(0, 0)
    print()
