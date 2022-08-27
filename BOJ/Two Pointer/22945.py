n = int(input())
arr = list(map(int, input().split()))
start, end = 0, n - 1
ans = 0
while start < end:
    team_ability = min(arr[start], arr[end]) * (end - start - 1)
    ans = max(ans, team_ability)
    if arr[start] < arr[end]:
        start += 1
    else:
        end -= 1

print(ans)
