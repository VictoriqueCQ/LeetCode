class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        res = 0
        nums.sort()
        for i in range(1, n):
            res = max(res, nums[i] - nums[i - 1])
        return res

