class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # 简化的 dp
        # r 代表当前位置是 r* 型要更改的次数
        # ry 代表当前位置是 r*y* 型要更改的次数
        # ryr 分别代表当前位置是 r*y*r* 型要更改的次数
        r, ry, ryr = int(leaves[0] == 'y'), float('inf'), float('inf')
        for i in range(1, len(leaves)):
            x = int(leaves[i] == 'y')
            r, ry, ryr = r+x, min(r, ry)+(1-x), min(ry, ryr)+x
        return ryr