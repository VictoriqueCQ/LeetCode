from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        for i, num in enumerate(nums):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))