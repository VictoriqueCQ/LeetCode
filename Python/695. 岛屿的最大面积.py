from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, self.dfs(grid, i, j))
        return max_area

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + self.dfs(grid, r + 1, c) + self.dfs(grid, r - 1, c) + self.dfs(grid, r, c + 1) + self.dfs(grid, r, c - 1)


s = Solution()
print(s.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
