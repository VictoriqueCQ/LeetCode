from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if 1 & i:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp
