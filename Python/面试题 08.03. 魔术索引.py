from typing import List
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            if i==nums[i]:
                return i
            if i<nums[i]:
                i=nums[i]
            else:
                i+=1
        return -1