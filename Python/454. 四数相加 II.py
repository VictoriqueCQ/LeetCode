class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = collections.Counter(a + b for a in A for b in B)
        return sum(dic.get(- c - d, 0) for c in C for d in D)

class Solution2:
    def fourSumCount(self, A, B, C, D):
        res = 0
        dic = {}
        for a in A:
            for b in B:
                total1 = a + b
                dic[total1] = dic.get(total1, 0) + 1
        for c in C:
            for d in D:
                total2 = c + d
                if -total2 in dic:
                    res += dic[-total2]
        return res

