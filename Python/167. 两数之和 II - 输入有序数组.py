from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # low, high = 0, len(numbers) - 1
        # while low < high:
        #     total = numbers[low] + numbers[high]
        #     if total == target:
        #         return [low + 1, high + 1]
        #     elif total < target:
        #         low += 1
        #     else:
        #         high -= 1
        #
        # return [-1, -1]
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                break
            elif sum < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]
