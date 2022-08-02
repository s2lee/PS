def promising(i):
    for k in range(0, i):
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
    return True


def solve(i):
    global answer

    if i == n:
        answer += 1
    else:
        for j in range(n):
            col[i] = j
            if promising(i):
                solve(i + 1)


n = int(input())
col = [0] * n
answer = 0
solve(0)
print(answer)
