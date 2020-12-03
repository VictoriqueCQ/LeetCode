class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a, b = 0, 0
        while b < len(typed) and a < len(name):
            if a == b == 0:
                if name[a] != typed[b]:  # 加速判断
                    return False
                a += 1
                b += 1
            else:
                if name[a] != typed[b]:
                    if typed[b] == typed[b - 1]:
                        while b < len(typed) and typed[b] == typed[b - 1]:  # 去重
                            b += 1
                    else:  # 加速判断
                        return False
                else:
                    a += 1
                    b += 1

        while b < len(typed):  # 边界复检1
            if typed[b] != typed[b - 1]:
                return False
            b += 1

        return True if a == len(name) else False  # 边界复检2

class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = 0
        b = 0
        while b < len(typed):
            if a < len(name) and name[a] == typed[b]:
                a += 1
                b += 1
            elif b > 0 and typed[b] == name[a - 1]:  # 这里也可以用  “一号 > 0” 或者 官方的 "typed[二号] == typed[二号 - 1]"
                b += 1
            else:
                return False
        return a == len(name)

