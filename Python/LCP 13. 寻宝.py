import collections
from typing import List
class Solution:
    def bfs(self, x, y, maze):
        delta = [0, 1, 0, -1, 0]
        m, n = len(maze), len(maze[0])
        res = [[-1] * n for _ in range(m)]
        res[x][y] = 0
        q = collections.deque()
        q.append([x, y])
        while q:
            temp = q.popleft()
            tx, ty = temp[0], temp[1]
            for k in range(1, 5):
                ttx, tty = tx + delta[k - 1], ty + delta[k]
                if ttx >= 0 and ttx < m and tty >= 0 and tty < n and maze[ttx][tty] != '#' and res[ttx][tty] == -1:
                    res[ttx][tty] = res[tx][ty] + 1
                    q.append([ttx, tty])
        return res

    def minimalSteps(self, maze: List[str]) -> int:
        m, n, sx, sy, tx, ty = len(maze), len(maze[0]), 0, 0, 0, 0
        buttons, stones = [], []
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'M':
                    buttons.append([i, j])
                elif maze[i][j] == 'O':
                    stones.append([i, j])
                elif maze[i][j] == 'S':
                    sx = i
                    sy = j
                elif maze[i][j] == 'T':
                    tx = i
                    ty = j
        nb, ns = len(buttons), len(stones)
        start_dist = self.bfs(sx, sy, maze)
        if not nb: return start_dist[tx][ty]

        dist = [[-1] * (nb + 2) for _ in range(nb)]
        dd = [[[]] for _ in range(nb)]
        for i in range(nb):
            d = self.bfs(buttons[i][0], buttons[i][1], maze)
            dd[i] = d
            dist[i][nb + 1] = d[tx][ty]
        for i in range(nb):
            temp = -1
            for k in range(ns):
                midx, midy = stones[k][0], stones[k][1]
                if start_dist[midx][midy] != -1 and dd[i][midx][midy] != -1:
                    if temp == -1 or temp > start_dist[midx][midy] + dd[i][midx][midy]:
                        temp = start_dist[midx][midy] + dd[i][midx][midy]
            dist[i][nb] = temp

            for j in range(i + 1, nb):
                temp = -1
                for k in range(ns):
                    midx, midy = stones[k][0], stones[k][1]
                    if dd[i][midx][midy] != -1 and dd[j][midx][midy] != -1:
                        if temp == -1 or temp > dd[j][midx][midy] + dd[i][midx][midy]:
                            temp = dd[j][midx][midy] + dd[i][midx][midy]
                dist[i][j] = temp
                dist[j][i] = temp

        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb + 1] == -1:
                return -1

        dp = [[-1] * nb for _ in range(1 << nb)]
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        for mask in range(1, 1 << nb):
            for i in range(nb):
                if (mask & (1 << i)) != 0:
                    for j in range(nb):
                        if not (mask & (1 << j)):
                            nx = mask | (1 << j)
                            if dp[nx][j] == -1 or dp[nx][j] > dp[mask][i] + dist[i][j]:
                                dp[nx][j] = dp[mask][i] + dist[i][j]

        res, final_mask = -1, (1 << nb) - 1
        for i in range(nb):
            if res == -1 or res > dp[final_mask][i] + dist[i][nb + 1]:
                res = dp[final_mask][i] + dist[i][nb + 1]
        return res