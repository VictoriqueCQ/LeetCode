class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        flag = True
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                flag = False
        return flag

        # return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))