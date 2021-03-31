from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sumAll = sum(nums)
        if S > sumAll or (S + sumAll) % 2 == 1:
            return 0
        target = (S + sumAll) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[-1]
