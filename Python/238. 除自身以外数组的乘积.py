class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        k = 1
        for i in range(len(nums)):
            result[i] = k
            k *= nums[i]
        k = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= k
            k *= nums[i]
        return result

s = Solution()
print(s.productExceptSelf([1,2,3,4]))