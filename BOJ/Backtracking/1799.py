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
