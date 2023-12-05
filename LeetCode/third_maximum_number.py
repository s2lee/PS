class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        first = nums[0]
        second = float("-inf")
        third = float("-inf")

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num

            elif second < num < first:
                third = second
                second = num

            elif third < num < second:
                third = num

        return third if third != float("-inf") else first


"""
O(nlogn)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)

        result = [*set(nums)]
        nums.sort() 
        return nums[-3]
"""
