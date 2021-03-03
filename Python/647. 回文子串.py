class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res += 1
        return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] 代表 子串[i, j] 是否是一个 回文串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        # 枚举所有可能 因为代表子串 所以 i <= j
        for j in range(n):
            for i in range(0, j + 1):
                # 子串长度
                length = j - i + 1
                # 只有一个字符 直接就是一个回文串
                if length == 1:
                    dp[i][j] = True
                    count += 1
                # 两个字符 只有相等才是回文串
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 超过两个字符 首位相同 且除去首尾的子串是回文串 才是回文串
                if length > 2 and s[i] == s[j] and dp[i+1][j-1] is True:
                    dp[i][j] = True
                    count += 1
        return count



class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res
