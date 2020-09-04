class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0], )}
        for i in nums[1:]:
            pres.update({j+(i, ) for j in pres if j[-1] <= i})
            pres.add((i, ))
        return [list(i) for i in pres if len(i) > 1]

