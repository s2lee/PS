import sys

for _ in range(int(input())):
    p = sys.stdin.readline().strip()
    cnt = 0
    for x in p:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt == -1:
                break

    print('YES' if cnt == 0 else 'NO')
