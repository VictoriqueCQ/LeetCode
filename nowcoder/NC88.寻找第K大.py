# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        # write code here
        l = 0
        r = len(a) - 1
        target = len(a) - K
        while l < r:
            mid = self.quickSelection(a, l, r)
            if mid == target:
                return a[mid]
            if mid < target:
                l = mid + 1
            else:
                r = mid - 1
        return a[l]

    def quickSelection(self, nums, l, r):
        i = l + 1
        j = r
        while True:
            while i < r and nums[i] <= nums[l]:
                i += 1
            while l < j and nums[j] >= nums[l]:
                j -= 1
            if i >= j:
                break
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        temp = nums[l]
        nums[l] = nums[j]
        nums[j] = temp
        return j
