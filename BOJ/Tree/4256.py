def solve(root, start, end):
    for i in range(start, end):
        if in_order[i] == pre_order[root]:
            solve(root + 1, start, i)
            solve(root + i + 1 - start, i + 1, end)
            print(pre_order[root], end=' ')
            return


for times in range(int(input())):
    N = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    solve(0, 0, N)
    print()