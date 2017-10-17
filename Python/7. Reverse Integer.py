# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
# python2 solution:
# class Solution:
#     # @return an integer
#     def reverse(self, x):
#         revx = int(str(abs(x))[::-1])
#         if revx > math.pow(2, 31):
#             return 0
#         else:
#             return revx * cmp(x, 0)

class Solution:
    def reverse(self,x):
        a = int(str(abs(x))[::-1])
        if a > pow(2,31):
            return 0
        else:
            if x>0:
                return a
            if x<0:
                return a*(-1)
            if x==0:
                return 0

s = Solution()
print(s.reverse(100))
print(s.reverse(-100))
print(s.reverse(pow(2,32)))