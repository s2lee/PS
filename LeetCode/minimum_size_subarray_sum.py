class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0

        start, ans, sum_value = 0, len(nums) + 1, 0
        for end, number in enumerate(nums):
            sum_value += number

            while sum_value >= target:
                ans = min(ans, end - start + 1)
                sum_value -= nums[start]
                start += 1

        return ans

