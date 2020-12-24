class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return (lambda dp, i: dp(dp,i,set(wordDict),set(map(len,wordDict))))(lambda dp, i, wordDict, lengths, cache = {len(s): ['']}: cache[i] if i in cache else [s[i:i+l] + (ws and ' ' + ws) for l in lengths if s[i:i+l] in wordDict for ws in cache.setdefault(i+l, dp(dp, i+l, wordDict, lengths, cache))], 0)

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        import functools
        if not wordDict:return []
        wordDict = set(wordDict)
        max_len = max(map(len, wordDict))
        @functools.lru_cache(None)
        def helper(s):
            res = []
            if not s:
                res.append("")
                return res
            for i in range(len(s)):
                if i < max_len and s[:i+1] in wordDict:
                    for t in helper(s[i+1:]):
                        if not t:
                            res.append(s[:i+1])
                        else:
                            res.append(s[:i+1] + " " + t)
            return res
        return helper(s)
