from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            dp[i] = max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[len(nums)]