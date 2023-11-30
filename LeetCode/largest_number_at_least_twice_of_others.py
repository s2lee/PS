class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        first_max = second_max = -1
        max_idx = 0

        for i, num in enumerate(nums):
            if num >= first_max:
                first_max, second_max = num, first_max
                max_idx = i
            elif num > second_max:
                second_max = num

        if first_max < 2 * second_max:
            max_idx = -1

        return max_idx


"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = max(nums)
        idx = 0
        for i in range(len(nums)):
            if max_value == nums[i]:
                idx = i
            else:
                if nums[i] * 2 > max_value:
                    return -1

        return idx
"""
