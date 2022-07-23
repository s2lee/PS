def check(num):
    num = list(str(num))
    for x in num:
        if x in broken:
            return False
    return True


n = int(input())
m = int(input())
broken = list(input().split())
result = abs(n - 100)
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i - n))

print(result)
