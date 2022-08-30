n = int(input())
arr = sorted(map(int, input().split()))
tmp = float('inf')
ans = [0] * 3

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        sum_value = arr[i] + arr[left] + arr[right]
        if abs(sum_value) < tmp:
            tmp = abs(sum_value)
            ans = [arr[i], arr[left], arr[right]]

        if sum_value > 0:
            right -= 1
        elif sum_value < 0:
            left += 1
        else:
            ans = [arr[i], arr[left], arr[right]]
            print(*sorted(ans))
            exit()

print(*sorted(ans))
