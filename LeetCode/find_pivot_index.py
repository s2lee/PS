class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            right_sum -= ele
            if left_sum == right_sum:
                return idx
            left_sum += ele
        return -1


"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_value = 0
        for i in range(len(nums)):
            if sum_value == sum(nums[i + 1:]):
                return i
            else:
                sum_value += nums[i]
        return -1

"""
