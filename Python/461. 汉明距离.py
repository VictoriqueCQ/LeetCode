class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        num = 0
        res = []
        while x != 0 or y != 0:
            res.append((x%2, y%2))
            x //= 2
            y //= 2
            print(res)
        for xii, yii in res:
            if xii != yii:
                num += 1
        return num

s = Solution()
s.hammingDistance2(1,4)