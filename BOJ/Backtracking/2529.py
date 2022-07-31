k = int(input())
sign_arr = input().split()
cache = [False] * 10
result = []


def possible(i, j, sign):
    if sign == '<':
        return i < j
    else:
        return i > j


def solve(idx, s):
    if idx == k + 1:
        result.append(s)
        return

    for num in range(10):
        if not cache[num]:
            if idx == 0 or possible(s[-1], str(num), sign_arr[idx - 1]):
                cache[num] = True
                solve(idx + 1, s + str(num))
                cache[num] = False


solve(0, "")
print(result[-1])
print(result[0])
