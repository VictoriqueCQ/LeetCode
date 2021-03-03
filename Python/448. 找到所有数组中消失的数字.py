from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        length = len(nums)
        res = list()
        for i in range(1,length+1):
            if i not in nums_set:
                res.append(i)
        return res