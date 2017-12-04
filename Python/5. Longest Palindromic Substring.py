# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        if lens < 2:
            return s
        maxlen = 0
        maxl = 0
        maxr = 0
        i = 0
        while i < lens:
            if (lens - i) < maxlen // 2:
                break
            j = i
            k = i
            while (k < lens - 1) and (s[k + 1] == s[j]):  # 寻找最大相同字符的子串作为核
                k = k + 1
            i = k + 1  # 跳过同一核中的其他i
            while (j > 0) and (k < lens - 1) and (s[j - 1] == s[k + 1]):
                j = j - 1
                k = k + 1
            if k - j + 1 > maxlen:
                maxlen = k - j + 1
                maxl = j
                maxr = k
        return s[maxl:maxr + 1]

s = Solution()
print(s.longestPalindrome("cababad"))