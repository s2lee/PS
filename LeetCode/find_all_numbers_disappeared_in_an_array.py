class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])

        return [i + 1 for i, n in enumerate(nums) if n > 0]


"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = list(set(range(1, len(nums) + 1)) - set(nums))
        return nums
"""
