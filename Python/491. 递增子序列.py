from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0], )}
        for i in nums[1:]:
            pres.update({j+(i, ) for j in pres if j[-1] <= i})
            pres.add((i, ))
        return [list(i) for i in pres if len(i) > 1]

# s = Solution()
# print(s.findSubsequences([4, 6, 7, 7]))
# a = {(4,)}
# a.update({(4,)+(6,)})
# print(a)