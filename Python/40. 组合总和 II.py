class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(res, tmp, can, tar):
            if tar == 0:
                res.append(tmp)
                return
            n = len(can)
            for i in range(n):   # 排序完之后避免在同一层中使用相同的元素
                if tar >= can[i] and not(i > 0 and can[i] == can[i - 1]):
                    helper(res, tmp + [can[i]], can[i + 1:], tar - can[i])

        res = []
        tmp = []
        candidates.sort()    # 先排序
        helper(res, tmp, candidates, target)
        return res