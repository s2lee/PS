class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums = set()
        for x in arr:
            if x * 2 in nums or x / 2 in nums:
                return True
            nums.add(x)
        return False


"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                    return True
        return False

"""
