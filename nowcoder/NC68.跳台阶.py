class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        dp = [0] * (number+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,number+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[number]
s = Solution()
print(s.jumpFloor(3))