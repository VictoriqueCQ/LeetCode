class Solution:
    def isValid(self , s ):
        # write code here
        a_dict = {"}":"{","]":"[",")":"("}
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i in a_dict.values():
                    stack.append(i)
                elif a_dict[i] == stack[-1]:
                    stack.pop()
        if not stack:
            return True
        else:
            return False
s= Solution()
print(s.isValid("(("))