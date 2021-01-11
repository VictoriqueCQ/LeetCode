class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if set(s)==set(' ') or set():
            return 0
        a = s.split()
        return len(a[-1])

