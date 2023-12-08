class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0

        for elem in nums:
            if elem == 0:
                current_consecutive = 0
            else:
                current_consecutive += 1
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
        return max_consecutive


"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_value = 0
        sum_value = 0
        for x in nums:
            if x == 1:
                sum_value += 1
            else:
                sum_value = 0
            max_value = max(max_value, sum_value)

        return max_value
"""
