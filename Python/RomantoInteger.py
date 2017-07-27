# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    def romanToInt(self, s):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        for i in range(len(s)):
            if i > 0 and val[s[i]] > val[s[i - 1]]:
                ret += val[s[i]] - 2 * val[s[i - 1]]
            else:
                ret += val[s[i]]
        return ret

s = Solution()
print(s.romanToInt("IV"))