class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_value = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = max_value
            if max_value < tmp:
                max_value = tmp

        arr[-1] = -1
        return arr
