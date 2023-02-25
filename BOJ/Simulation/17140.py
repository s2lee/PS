from collections import Counter
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
ans = 0


def calculate_r_c(arr: list, is_r: bool) -> list:
    if not is_r:
        arr = list(zip(*arr))

    result = []
    max_arr_length = -1
    for x in arr:
        x = [i for i in x if i != 0]
        count = Counter(x).most_common()
        count.sort(key=lambda t: (t[1], t[0]))
        max_arr_length = max(max_arr_length, len(count) * 2)
        c_arr = []
        for ct in count:
            c_arr.extend(ct)

        result.append(c_arr)
    for x in result:
        zero_cnt = max_arr_length - len(x)
        if zero_cnt > 0:
            x.extend([0] * zero_cnt)

    if not is_r:
        result = list(zip(*result))
    return result


while ans <= 100:
    if len(array) > r - 1 and len(array[0]) > c - 1:
        if array[r - 1][c - 1] == k:
            break

    array = calculate_r_c(array, len(array) >= len(array[0]))
    ans += 1

print(ans if ans <= 100 else -1)
