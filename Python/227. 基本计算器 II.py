class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10*num + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:#除法取整中（a//b为向下取整），当被除数（a）为负时，不单独做判断会出错！！！
                #如(2//3 = 0)，但(-2//3 = -1)，而实际我们希望得到的是
                # -(2//3) = -0 = 0，增加负数判断即可
                    tmp = stack.pop()
                    tmp_sign = 1 if tmp >= 0 else -1
                    stack.append(tmp_sign*(abs(tmp)//num))
                num = 0
                sign = s[i]
        return sum(stack)

s = Solution()
print(s.calculate("3+2*2"))