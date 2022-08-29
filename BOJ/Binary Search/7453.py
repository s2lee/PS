n = int(input())
A, B, C, D = [[0] * n for _ in range(4)]
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split())

AB = sorted(i + j for i in A for j in B)
CD = sorted(i + j for i in C for j in D)

ans = 0
start, end = 0, n * n - 1
while start < n * n and end >= 0:
    if AB[start] + CD[end] > 0:
        end -= 1
    elif AB[start] + CD[end] < 0:
        start += 1
    else:
        p, q = start, end
        while start < n * n and AB[start] == AB[p]:
            start += 1

        while end >= 0 and CD[end] == CD[q]:
            end -= 1
        ans += (start - p) * (q - end)

print(ans)
