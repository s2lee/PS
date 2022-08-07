def dfs(s):
    for i in range(1, len(s)//2 + 1):
        if s[-i:] == s[2 * -i:-i]:
            return

    if len(s) == n:
        print(s)
        exit(0)

    for num in ['1', '2', '3']:
        dfs(s + num)


n = int(input())
dfs('1')