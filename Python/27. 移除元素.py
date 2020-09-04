# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        count = 0
        result = []
        while index < len(nums):
            if nums[index] != val:
                # result.append(nums[index])
                nums[count] = nums[index]
                count += 1
            index += 1
        return count

nums = [3,2,2,3]
s = Solution()
val = 3
print(s.removeElement(nums,val))