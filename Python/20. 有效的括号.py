# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     pars = [None]
    #     parmap = {')': '(', '}': '{', ']': '['}
    #     for c in s:
    #         if c in parmap and parmap[c] == pars[len(pars) - 1]:
    #             pars.pop()
    #         else:
    #             pars.append(c)
    #     return len(pars) == 1

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            # print("i:"+c)
            if c in parmap:
                # print("c:"+c)
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1


s = Solution()
str = "(){}[]"
print(s.isValid(str))