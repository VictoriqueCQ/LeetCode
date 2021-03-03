from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        for i in g:
            for j in range(len(s)):
                if s[j] >= i:
                    count += 1
                    s.remove(s[j])
                    break
        return count
        # j = 0
        # for i in range(len(s)):
        #     if s[i] >= g[j]:
        #         j += 1
        #     if j == len(g): return j
        # return j
s = Solution()
print(s.findContentChildren([1,2,3],[1,3]))