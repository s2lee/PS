n = int(input())
snow = list(map(int, input().split()))

snow.sort()
ans = float('inf')
for i in range(n - 3):
    for j in range(i + 3, n):
        target = snow[i] + snow[j]
        left, right = i + 1, j - 1
        while left < right:
            sum_value = snow[left] + snow[right]
            if abs(target - sum_value) < ans:
                ans = abs(target - sum_value)

            if sum_value < target:
                left += 1
            elif sum_value > target:
                right -= 1
            else:
                print(0)
                exit()

print(ans)