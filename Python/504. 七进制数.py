class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        is_negative = num < 0
        if is_negative:
            num = -num
        ans = ""
        while num:
            a = num // 7
            b = num % 7
            ans = str(b)+ans
            num = a
        if is_negative:
            ans = "-" + ans
        return ans