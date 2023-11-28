class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        fix = len(arr)
        idx = 0
        while idx < fix:
            if arr[idx] == 0:
                arr.insert(idx, 0)
                idx += 2
            else:
                idx += 1 

        for _ in range(len(arr) - fix):
            arr.pop()

"""
