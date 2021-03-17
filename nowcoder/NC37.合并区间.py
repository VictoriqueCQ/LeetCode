# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals ):
        # write code here
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
