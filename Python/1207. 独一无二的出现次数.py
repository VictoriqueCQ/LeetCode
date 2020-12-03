class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cishu = {}

        for i in arr:
            if i not in cishu:
                cishu[i] = 1
            else:
                cishu[i] += 1

        CishudeCishu = {}

        for j in cishu:
            if cishu[j] in CishudeCishu:
                return False
            else:
                CishudeCishu[cishu[j]] = 1

        return True

