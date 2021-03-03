from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [0]*n
        if n < 3: return 0
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
        count = 0
        for i in dp:
            count += i
        return count