class Solution:
    def reverseBits(self, n: int) -> int:
        print(("0"*32+bin(n)[2:]))
        print(("0"*32+bin(n)[2:])[-32:])
        return int("0b"+("0"*32+bin(n)[2:])[-32:][::-1], base=2)

a = Solution()
print(a.reverseBits(43261596))