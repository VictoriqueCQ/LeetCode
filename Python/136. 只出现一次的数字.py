from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(lambda x, y: x ^ y, nums)
        sum1 = sum(nums)
        sum2 = sum(set(nums))*2
        return sum2-sum1


