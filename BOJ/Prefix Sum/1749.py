import sys
input = sys.stdin.readline


def solve(v):
    result, dp = v[0], v[0]
    for i in range(1, len(v)):
        dp = max(dp + v[i], v[i])
        result = max(result, dp)
    return result


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(1, m):
        matrix[i][j] += matrix[i][j - 1]

max_value = -1e9
for k in range(m):
    for r in range(k, m):
        prefix_sum = [matrix[i][r] - (matrix[i][k - 1] if k else 0) for i in range(n)]
        max_value = max(max_value, solve(prefix_sum))

print(max_value)
