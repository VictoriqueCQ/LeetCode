from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(isConnected,i,visited)
                count += 1
        return count

    def dfs(self,isConnected:List[List[int]],i:int,visited:set):
        for j in range(len(isConnected)):
            if isConnected[i][j]==1 and j not in visited:
                visited.add(j)
                self.dfs(isConnected, j, visited)
s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))