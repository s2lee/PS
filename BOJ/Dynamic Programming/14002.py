import sys
input = sys.stdin.readline


def find_idx(value):
    result = 0
    idx = 0
    length = len(array)
    while idx <= length:
        mid = (idx + length)//2
        if array[mid] >= value:
            result = mid
            length = mid - 1
        else:
            idx = mid + 1
    return result


N = int(input())
A = list(map(int, input().split()))
B = [1]

array = [A[0]]
for i in range(1, N):
    if A[i] > array[-1]:
        array.append(A[i])
        B.append(len(array))
    else:
        tmp = find_idx(A[i])
        array[tmp] = A[i]
        B.append(tmp+1)

tmp_max = max(B)
C = []
for i in range(len(B)-1, -1, -1):
    if tmp_max == 0:
        break
    if B[i] == tmp_max:
        C.append(A[i])
        tmp_max -= 1

print(len(array))
print(*C[::-1])
