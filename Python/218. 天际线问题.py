from typing import List
class Solution:
    def getSkyline(self, buildings):
        import heapq
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, 0) for _, R, _ in buildings } ))
        res = [[0, 0]]
        heap = [[0, float("inf")]]
        for x, H, R in events:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if H:
                heapq.heappush(heap, [H, R])
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]

class Solution1:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]

        for x, h in loc:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])

        return res[1:]

