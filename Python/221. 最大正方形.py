from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        # m = len(matrix)
        # n = len(matrix[0])
        # max_side = 0
        # dp = [[0] * (n + 1)] * (m + 1)
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if matrix[i-1][j-1]=='1':
        #             if i==0 or j == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
        #         max_side = max(dp[i][j],max_side)
        # print(dp)
        # return max_side**2
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        print(dp)
        maxSquare = maxSide * maxSide
        return maxSquare

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],
                       ["1","0","1","1","1"],
                       ["1","1","1","1","1"],
                       ["1","0","0","1","0"]]))
