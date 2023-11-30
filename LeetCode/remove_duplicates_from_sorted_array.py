class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[idx] = nums[i + 1]
                idx += 1

        return idx


"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for elem in nums[1:]:
            if nums[slow] != elem:
                slow += 1
                nums[slow] = elem
        return slow + 1

O(nlogn)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

nums =  doesn't replace elements in the original list.
nums[:] = replaces element in place

O(n^2)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elem = set()
        i = 0
        while i < len(nums):
            if nums[i] in elem:
                nums.remove(nums[i])
            else:
                elem.add(nums[i])
                i += 1

        return len(nums)

"""
