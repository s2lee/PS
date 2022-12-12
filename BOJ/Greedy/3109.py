r, c = map(int, input().split())

b_map = []
for i in range(r):
    temp = list(input())
    b_map.append(temp)


def dfs(y, x):
    stack = [[y, x]]
    while stack:
        y, x = stack[-1]
        b_map[y][x] = 'O'
        if x == c - 1:
            return True
        if x + 1 < c and y - 1 >= 0 and b_map[y - 1][x + 1] == '.':
            x += 1
            y -= 1
            stack.append([y, x])
            continue
        elif x + 1 < c and b_map[y][x + 1] == '.':
            x += 1
            stack.append([y, x])
            continue
        elif x + 1 < c and y + 1 < r and b_map[y + 1][x + 1] == '.':
            x += 1
            y += 1
            stack.append([y, x])
            continue
        else:
            stack.pop()
    return False


answer = 0
for i in range(r):
    if dfs(i, 0):
        answer += 1

print(answer)