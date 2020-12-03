from typing import List
import math


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x:x*x,A))
        # res = []
        # for i in A:
        #     a = i*i
        #     res.append(a)
        # res = sorted(res)
        # return sorted([k ** 2 for k in A])


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
