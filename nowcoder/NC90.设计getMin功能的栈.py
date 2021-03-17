#
# return a array which include all ans for op3
# @param op int整型二维数组 operator
# @return int整型一维数组
#
class Solution:
    def getMinStack(self , op ):
        # write code here
        stack = []
        res = []
        for i in op:
            if i[0] == 1:
                stack.append(i[1])
            elif i[0] == 2:
                stack.pop()
            elif i[0] ==3:
                res.append(min(stack))
        return res