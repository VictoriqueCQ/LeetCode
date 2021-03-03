from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        res = 0
        max_ = arr[0]
        for idx, num in enumerate(arr):
            max_ = max(max_, num)
            if idx >= max_: res += 1
        return res
