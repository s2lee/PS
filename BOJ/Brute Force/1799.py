import sys


def solve(row, col, count, color):
    global answer
    if col >= n:
        row += 1
        col = 1 if not col % 2 else 0

    if row >= n:
        answer[color] = max(answer[color], count)
        return

    if chess[row][col] and not check_w[row + col] and not check_b[row - col + n - 1]:
        check_w[row + col] = check_b[row - col + n - 1] = 1
        solve(row, col + 2, count + 1, color)
        check_w[row + col] = check_b[row - col + n - 1] = 0

    solve(row, col + 2, count, color)


n = int(input())
chess = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check_b = [0] * (2 * n - 1)
check_w = [0] * (2 * n - 1)
answer = [0, 0]

solve(0, 0, 0, 0)
solve(0, 1, 0, 1)
print(sum(answer))

"""
def solve(count, start, color):
    global answer
    if start == available_cnt[color]:
        answer[color] = max(answer[color], count)
    else:
        for i in range(start, available_cnt[color]):
            x, y = available[color][i]
            if not check_w[x + y] and not check_b[x - y + n - 1]:
                check_w[x + y] = check_b[x - y + n - 1] = 1
                solve(count + 1, i + 1, color)
                check_w[x + y] = check_b[x - y + n - 1] = 0


n = int(input())
available = [[], []]
available_cnt = [0, 0]
check_b = [0] * (2 * n - 1)
check_w = [0] * (2 * n - 1)
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] == 1:
            if (i + j) % 2 == 0:
                available[0].append((i, j))
                available_cnt[0] += 1
            else:
                available[1].append((i, j))
                available_cnt[1] += 1

answer = [0, 0]
solve(0, 0, 0)
solve(0, 0, 1)
print(sum(answer))
"""