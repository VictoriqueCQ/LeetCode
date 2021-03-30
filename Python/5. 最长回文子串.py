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

class Solution2:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
