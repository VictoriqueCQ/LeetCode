from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals,key=lambda x:x[1])
        count = 1
        end = intervals[0][1]
        for a, b in intervals:
            if a>=end:
                count += 1
                end = b
        return len(intervals)-count
s = Solution()
print(s.eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]]))