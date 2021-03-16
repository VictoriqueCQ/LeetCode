#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self , s , t ):
        mlen = max(len(s), len(t))
        s = s.zfill(mlen)
        t = t.zfill(mlen)
        plus = 0
        res = ""
        for i in range(-1, -mlen-1, -1):
            last = ord(s[i]) + ord(t[i]) - ord("0") + plus
            if last > ord("9"):
                plus = 1
                res += chr(last - 10)
            else:
                plus = 0
                res += chr(last)
        if plus: res += str(plus)
        return res[::-1]
        # write code here