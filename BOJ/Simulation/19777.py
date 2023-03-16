n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(1, n):
        array[i][j] += array[i][j - 1]

total = sum(row[-1] for row in array)

answer = float("inf")
for d1 in range(1, n - 2):
    for d2 in range(1, n - 1 - d1):
        for x in range(n - d1 - d2):
            for y in range(d1, n - d2):
                p1, p2, p3, p4 = 0, 0, 0, 0
                for i in range(x):
                    p1 += array[i][y]
                    p2 += array[i][-1] - array[i][y]

                for i in range(x, x + d1):
                    p1 += array[i][y - 1 - i + x]

                for i in range(x, x + d2 + 1):
                    p2 += array[i][-1] - array[i][y + i - x]

                for i in range(x + d1, x + d1 + d2 + 1):
                    p3 += array[i][y - d1 - 1 + i - x - d1] if y - d1 else 0

                for i in range(x + d2 + 1, x + d1 + d2 + 1):
                    p4 += array[i][-1] - array[i][y + d2 - i + x + d2]

                for i in range(x + d1 + d2 + 1, n):
                    p3 += array[i][y - d1 + d2 - 1]
                    p4 += array[i][-1] - array[i][y - d1 + d2 - 1]

                a, _, _, _, b = sorted([p1, p2, p3, p4, total - p1 - p2 - p3 - p4])
                answer = answer if b - a > answer else b - a

print(answer)
