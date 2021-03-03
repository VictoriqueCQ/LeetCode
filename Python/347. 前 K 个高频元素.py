from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        a = collections.Counter(nums)
        a = dict(a)
        a = sorted(a.items(),key=lambda x:x[1],reverse=True)
        b = []
        for i in range(k):
            b.append(a[i][0])
        print(b)
        # for e in collections.Counter(nums).most_common(k):
        #     print(e[0])
        return [e[0] for e in collections.Counter(nums).most_common(k)]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3,3,3], 2))