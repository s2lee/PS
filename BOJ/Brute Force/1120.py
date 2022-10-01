a, b = input().split()
min_cnt = 51
for i in range(len(b) - len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)
