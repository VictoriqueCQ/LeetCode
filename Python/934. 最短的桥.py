class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(x,y):
            A[x][y]=2
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=nx<len(A) and 0<=ny<len(A[0]) and A[nx][ny]==1:
                    q.append([nx,ny])
                    dfs(nx,ny)
        flag,cnt,q=True,0,collections.deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    flag=False
                    q.append([i,j])
                    dfs(i,j)
                    break
            if not flag:
                break
        while q:
            size=len(q)
            for _ in range(size):
                x,y=q.popleft()
                for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if 0<=nx<len(A) and 0<=ny<len(A[0]) and A[nx][ny]==1:
                        return cnt
                    if 0<=nx<len(A) and 0<=ny<len(A[0]) and A[nx][ny]==0:
                        A[nx][ny]=2
                        q.append([nx,ny])
            cnt+=1
        return cnt
