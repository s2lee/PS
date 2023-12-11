class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
            else:
                nums.append(0)

        for _ in range(length - idx):
            nums.pop()

        for i in range(idx, length) :
            nums[i] = 0
"""
