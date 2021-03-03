from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                # pop the smaller value's index
                small = stack.pop()
                res[small] = i - small

            # append the index of current value
            stack.append(i)

        return res

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))