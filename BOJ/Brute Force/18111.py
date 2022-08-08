n, m, b = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
time, height = 1e9, 0
for target in range(257):
    inventory_up, inventory_down = 0, 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < target:
                inventory_down += (target - table[j][k])
            else:
                inventory_up += (table[j][k] - target)

    if inventory_up + b < inventory_down:
        continue

    temp = 2 * inventory_up + inventory_down
    if temp <= time:
        time = temp
        height = target

print(time, height)
