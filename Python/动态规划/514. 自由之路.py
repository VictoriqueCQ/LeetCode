import collections
import functools
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dic = collections.defaultdict(set)
        for i, char in enumerate(ring):
            dic[char].add(i)
        n = len(key)
        m = len(ring)

        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0: return min(j, m - j) + 1
            res = float('inf')
            for k in dic[key[i - 1]]:
                res = min(res, 1 + dp(i - 1, k) + min(abs(k - j), abs(j + m - k), abs(k + m - j)))
            return res

        return min(dp(n - 1, j) for j in dic[key[n - 1]])


