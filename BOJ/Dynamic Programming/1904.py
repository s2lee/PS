n = int(input())
a, b, c = 1, 2, 0
cnt = 2

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    while True:
        if cnt == n:
            break
        c = (a + b) % 15746
        a, b = b, c
        cnt += 1
    print(c)
