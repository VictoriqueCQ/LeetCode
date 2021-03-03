from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0: return []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    a = 99999
                    b = 99999
                    if j > 0:
                        a= matrix[i][j - 1] + 1
                    if i > 0:
                        b = matrix[i - 1][j] + 1
                    matrix[i][j] = min(a,b)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    a = 99999
                    b = 99999
                    if j < n - 1:
                        a= matrix[i][j + 1] + 1
                    if i < m - 1:
                        b = matrix[i + 1][j] + 1
                    matrix[i][j] = min(matrix[i][j],min(a, b))
        return matrix

s = Solution()
print(s.updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]]))