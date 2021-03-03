from typing import List
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    # def extreme_insertion_index(self, nums, target, left):
    #     lo = 0
    #     hi = len(nums)
    # 
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if nums[mid] > target or (left and target == nums[mid]):
    #             hi = mid
    #         else:
    #             lo = mid+1
    # 
    #     return lo
    # 
    # 
    # def searchRange(self, nums, target):
    #     left_idx = self.extreme_insertion_index(nums, target, True)
    # 
    #     # assert that `left_idx` is within the array bounds and that `target`
    #     # is actually in `nums`.
    #     if left_idx == len(nums) or nums[left_idx] != target:
    #         return [-1, -1]
    # 
    #     return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_first(nums,target)
        right = self.find_last(nums,target)
        print(left, right)
        if left > right:
            return [-1,-1]
        else:
            return [left,right]

    def find_first(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def find_last(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return r

s = Solution()
print(s.searchRange([5,7,7,8,8,10],8))