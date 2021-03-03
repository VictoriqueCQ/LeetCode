from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # left = [1 for _ in range(len(ratings))]
        # right = left[:]
        # for i in range(1, len(ratings)):
        #     if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        # count = left[-1]
        # for i in range(len(ratings) - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
        #     count += max(left[i], right[i])
        # return count
        candy_list = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candy_list[i + 1] = candy_list[i] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy_list[i] <= candy_list[i+1]:
                candy_list[i] = candy_list[i+1] + 1
        count = 0
        for i in candy_list:
            count += i
        return count

s = Solution()
print(s.candy([1, 0, 2]))
