class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        idx = len(nums) - 1
        while idx >= 0:
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1
            idx -= 1
        return result


"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] **2

        nums.sort()
        return nums
"""
