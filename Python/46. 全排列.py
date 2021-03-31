from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # def backtrack(nums, tmp):
        #     print("nums:",end="")
        #     print(nums)
        #     print("tmp:",end="")
        #     print(tmp)
        #     if not nums:
        #         print("tmp:", end="")
        #         print(tmp)
        #         res.append(tmp)
        #         return
        #     for i in range(len(nums)):
        #         print(i, nums[:i], nums[i + 1:], nums[:i] + nums[i + 1:], tmp + [nums[i]])
        #         backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        #
        # backtrack(nums, [])
        res = [i for i in itertools.permutations(nums)]
        return res

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return list(itertools.permutations(nums))




s = Solution()
print(s.permute([1, 2, 3]))
