n = int(input())
array = list(map(int, input().split()))
sum_value = sum(array)
if sum_value % 4:
    print(0)
else:
    cnt = [0] * 4
    cnt[0] = 1
    prefix_sum = 0
    division = sum_value // 4
    for i in range(n - 1):
        prefix_sum += array[i]
        if prefix_sum == 3 * division:
            cnt[3] += cnt[2]
        if prefix_sum == 2 * division:
            cnt[2] += cnt[1]
        if prefix_sum == 1 * division:
            cnt[1] += cnt[0]
    print(cnt[3])
