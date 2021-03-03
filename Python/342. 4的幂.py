class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        a = 1
        while a <= n:
            if a == n:
                return True
            else:
                a = 4*a
                i += 1
        return False