class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        charS = []
        charT = []
        for i in S:
            if i != '#':
                charS.append(i)
            else:
                if charS:
                    charS.pop()

        for j in T:
            if j != '#':
                charT.append(j)
            else:
                if charT:
                    charT.pop()

        return ''.join(charS) == ''.join(charT)


