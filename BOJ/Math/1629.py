def solve(a, b, c):
    if b == 1:
        return a % c
    else:
        x = solve(a, b // 2, c)
        if b % 2 == 0:
            return x * x % c
        else:
            return x * x * a % c


A, B, C = map(int, input().split())
print(solve(A, B, C))
