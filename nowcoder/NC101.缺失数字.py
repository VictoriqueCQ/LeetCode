#
# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型
#
class Solution:
    def solve(self , a ):
        # write code here
        n = len(a)
        for i in range(n):
            if i != a[i]:
                return i
        return n

s = Solution()
print(s.solve([0, 1, 2, 3, 4, 5, 7]))
