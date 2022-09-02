n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]

start, end = 0, max(time) * m
answer = 0
while start <= end:
    passed_person_cnt = 0
    mid = (start + end) // 2
    for t in time:
        passed_person_cnt += mid // t
    if passed_person_cnt < m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
