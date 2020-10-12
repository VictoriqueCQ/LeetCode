from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        return [e[0] for e in collections.Counter(nums).most_common(k)]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))