from typing import List
import heapq


class Solution:

    # 使用容量为 k 的小顶堆
    # 元素个数小于 k 的时候，放进去就是了
    # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换

    # def findKthLargest(self, nums: List[int], k: int) -> int:
        # size = len(nums)
        # if k > size:
        #     raise Exception('程序出错')
        #
        # L = []
        # for index in range(k):
        #     # heapq 默认就是小顶堆
        #     heapq.heappush(L, nums[index])
        #
        # for index in range(k, size):
        #     top = L[0]
        #     if nums[index] > top:
        #         # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
        #         heapq.heapreplace(L, nums[index])
        # # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        # return L[0]
    #     l = 0
    #     r = len(nums) - 1
    #     target = len(nums) - k
    #     while l < r:
    #         mid = self.quickSelection(nums, l, r)
    #         if mid == target:
    #             return nums[mid]
    #         if mid < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return nums[l]
    #
    # def quickSelection(self, nums, l, r):
    #     i = l + 1
    #     j = r
    #     while True:
    #         while i < r and nums[i] <= nums[l]:
    #             i += 1
    #         while l < j and nums[j] >= nums[l]:
    #             j -= 1
    #         if i >= j:
    #             break
    #         temp = nums[i]
    #         nums[i] = nums[j]
    #         nums[j] = temp
    #     temp = nums[l]
    #     nums[l] = nums[j]
    #     nums[j] = temp
    #     return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        key = nums[0]
        low = 0
        high = len(nums) - 1
        nums = self.quick_sort(nums, low, high)
        return nums[len(nums)-k]

    def quick_sort(self, nums, start, end):
        if start >= end: return nums
        low = start
        high = end
        key = nums[start]
        while low < high:
            while low < high and nums[high] >= key:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= key:
                low += 1
            nums[high] = nums[low]
        nums[low] = key
        self.quick_sort(nums, start, low - 1)
        self.quick_sort(nums, low + 1, end)
        return nums

s = Solution()
print(s.findKthLargest([1],1))
# print(s.quick_sort([1],0,0))