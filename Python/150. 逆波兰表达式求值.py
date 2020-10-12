class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        PopList = []
        for i in tokens:
            if i in "+-*/":
                tmp = PopList.pop()
                tmp2 = PopList.pop()
                PopList.append(str(int(eval(tmp2+i+tmp))))
            else:
                PopList.append(i)
        return int(PopList[0])

