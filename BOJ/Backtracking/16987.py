def solve(cur_egg, broken_eggs_num):
    global ans

    if cur_egg == n:
        ans = max(ans, broken_eggs_num)
        return

    if (n - cur_egg) * 2 + broken_eggs_num < ans:
        return

    if eggs[cur_egg][0] <= 0:
        solve(cur_egg + 1, broken_eggs_num)
    else:
        lonely_egg = True
        for i in range(n):
            if eggs[i][0] > 0 and i != cur_egg:
                lonely_egg = False
                eggs[i][0] -= eggs[cur_egg][1]
                eggs[cur_egg][0] -= eggs[i][1]
                temp = broken_eggs_num
                if eggs[i][0] <= 0:
                    temp += 1
                if eggs[cur_egg][0] <= 0:
                    temp += 1
                solve(cur_egg + 1, temp)
                eggs[i][0] += eggs[cur_egg][1]
                eggs[cur_egg][0] += eggs[i][1]
        if lonely_egg:
            solve(cur_egg + 1, broken_eggs_num)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0
solve(0, 0)
print(ans)
