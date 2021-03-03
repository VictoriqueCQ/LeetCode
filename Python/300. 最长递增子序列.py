from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 0
        n = len(nums)
        if n <= 1: return n
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            max_length = max(max_length,dp[i])
        return max_length

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))