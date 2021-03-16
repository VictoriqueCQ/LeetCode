#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self, arr):
        # write code here
        max = 0
        cur = 0
        for i in arr:
            cur += i
            if cur >= max:
                max = cur
            if cur < 0:
                cur = 0
        return max

s = Solution()
print(s.maxsumofSubarray([1, -2, 3, 5, -2, 6, -1]))
