class Solution:
    def reorganizeString(self, S: str) -> str:
        s = sorted(S)
        count = collections.Counter(S)
        s.sort(key=count.get)
        n = len(s) // 2
        if s[n - 1] == s[-1]:
            return ''

        a, b = s[:n], s[n:]
        for i in range(len(b)):
            s[i * 2] = b[i]
        for i in range(len(a)):
            s[i * 2 + 1] = a[i]

        return ''.join(s)