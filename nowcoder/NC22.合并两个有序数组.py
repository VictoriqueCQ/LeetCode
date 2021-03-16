#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        # A = A.sort()
        # B = B.sort()
        # while m > 0 and n > 0:
        #     if A[m - 1] > B[n - 1]:
        #         A[m + n - 1] = A[m - 1]
        #         m = m - 1
        #     else:
        #         A[m + n - 1] = B[n - 1]
        #         n = n - 1
        # return A
        A[:] = sorted(A[:m]+B)

s = Solution()
print(s.merge([],0,[1],1))