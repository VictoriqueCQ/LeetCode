class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n / 3
            print(n)
        return n == 1

s = Solution()
print(s.isPowerOfThree(45))