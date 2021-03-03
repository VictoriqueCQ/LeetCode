class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.preSum = [0]*(n+1)
        for i in range(1,n+1):
            self.preSum[i] = self.preSum[i-1]+nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j+1]-self.preSum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)