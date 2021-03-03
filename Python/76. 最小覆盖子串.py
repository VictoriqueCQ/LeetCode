import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        print(need)
        needCnt = len(t)
        i = 0 #记录起始位置
        res = (0, float('inf'))  #用两个元素，方便之后记录起终点
        #三步骤：
        #1. 增加右边界使滑窗包含t
        for j,c in enumerate(s):
            if need[c] >0:
                needCnt -= 1
            need[c] -= 1 #这行放在外面不可以，看19行 need[c] == 0
        #2. 收缩左边界直到无法再去掉元素   !注意，处理的是i
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0: #表示再去掉就不行了(need>0)
                        break
                    else:
                        need[c] += 1
                        i += 1
                if j-i < res[1] - res[0]:  #这里是否减一都可以，只要每次都是这样算的就行，反正最后也是输出子串而非长度
                    res = (i,j)
        #3. i多增加一个位置，准备开始下一次循环(注意这步是在 needCnt == 0里面进行的 )
                need[s[i]] += 1
                needCnt += 1    #由于 移动前i这个位置 一定是所需的字母，因此NeedCnt才需要+1
                i += 1
        return "" if res[1]>len(s) else s[res[0]: res[1]+1]

        # def minWindow(self, s: str, t: str) -> str:
        #     need = collections.defaultdict(int)
        #     for c in t:
        #         need[c] += 1
        #     needCnt = len(t)
        #     i = 0
        #     res = (0, float('inf'))
        #     for j, c in enumerate(s):
        #         if need[c] > 0:
        #             needCnt -= 1
        #         need[c] -= 1
        #         if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
        #             while True:  # 步骤二：增加i，排除多余元素
        #                 c = s[i]
        #                 if need[c] == 0:
        #                     break
        #                 need[c] += 1
        #                 i += 1
        #             if j - i < res[1] - res[0]:  # 记录结果
        #                 res = (i, j)
        #             need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
        #             needCnt += 1
        #             i += 1
        #     return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果

class Solution2:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import Counter
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            # print(start, end)
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1
        return res


class Solution3:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res

class Solution4:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        findout = defaultdict(int)
        for i in t:
            findout[i] += 1
        min_len, res = float('inf'), ""
        l, counter = len(s), len(t)
        left = right = 0
        #------------------------------
        while right < l:
            if findout[s[right]] > 0:
                counter -= 1
            findout[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if findout[s[left]] == 0:
                    counter += 1
                findout[s[left]] += 1
                left += 1
        #-------------------------------------
        return res



s = Solution4()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))