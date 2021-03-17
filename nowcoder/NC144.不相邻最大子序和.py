#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算
# @param n int整型 数组的长度
# @param array int整型一维数组 长度为n的数组
# @return long长整型
#
class Solution:
    def subsequence(self , n , array ):
        # write code here
        if n <= 2:
            return max(array)
        dp = [0] * n
        dp[0] = array[0]
        dp[1] = max(dp[0],array[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+array[i])
        return dp[n-1]