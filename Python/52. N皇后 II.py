class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[['.']*n for _ in range(n)]
        res=[]
        col,dl,dr=[0]*2*n,[0]*2*n,[0]*2*n
        def dfs(i):
            if i==n:
                li=[]
                for k in range(n):
                    li.append(''.join(board[k]))
                res.append(li)
            for j in range(n):
                if not col[j] and not dr[i-j] and not dl[i+j]:
                    col[j]=dr[i-j]=dl[i+j]=1
                    board[i][j]='Q'
                    dfs(i+1)
                    col[j]=dr[i-j]=dl[i+j]=0
                    board[i][j]='.'
        dfs(0)
        return len(res)

class Solution2:
    def totalNQueens(self, n: int) -> int:
        def back(i, rows, pie, na):
            if i == n:  ##已经到底了，则是满足条件
                return 1
            total = 0
            for j in range(n):
                if j in rows or i + j in pie or i - j in na:
                    continue
                total += back(i + 1, rows | {j}, pie | {i + j}, na | {i - j})
            return total

        return back(0, set(), set(), set())

