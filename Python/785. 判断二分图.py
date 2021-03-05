from typing import List
import collections
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # dfs time O(E+V), space O(V)
        n = len(graph)
        visited = [0] * n

        stack = []
        for i in range(n):
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1

                while stack:
                    cur = stack.pop()

                    for neighbor in graph[cur]:
                        if visited[neighbor] == 0:
                            stack.append(neighbor)
                            visited[neighbor] = -visited[cur]
                        else:
                            if visited[neighbor] != -visited[cur]:
                                return False
        return True


s = Solution1()
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))