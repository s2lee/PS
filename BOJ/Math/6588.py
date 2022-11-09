array = [1] * 1000001
for i in range(2, 1000001):
    j = 2
    while i * j < 1000001:
        if array[i * j]:
            array[i * j] = 0
        j += 1

array[1] = 0
while True:
    n = int(input())
    if n == 0:
        break

    check = True

    for x in range(n, 2, -1):
        if x % 2 == 1:
            if array[x]:
                if array[n - x]:
                    print(f'{n} = {n - x} + {x}')
                    check = False
                    break
    if check:
        print("Goldbach's conjecture is wrong.")
