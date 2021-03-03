from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        # 流向太平洋的位置
        res1 = set()
        # 流向大西洋的位置
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        # 从边界遍历
        def dfs(i, j, cur, res):
            res.add((i, j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[i][j] <= matrix[tmp_i][tmp_j] and (tmp_i, tmp_j) not in res:
                    dfs(tmp_i, tmp_j, matrix[i][j], res)
        # 太平洋
        for i in range(row):
            dfs(i, 0, 0, res1)
        # 太平洋
        for j in range(col):
            dfs(0, j, 0, res1)
        # 大西洋
        for i in range(row):
            dfs(i, col - 1, 0, res2)
        # 大西洋
        for j in range(col):
            dfs(row - 1, j, 0, res2)

        return res1 & res2
