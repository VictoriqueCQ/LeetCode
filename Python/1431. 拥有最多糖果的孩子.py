class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if max(candies) == candies[i]:
                result.append(True)
            else:
                result.append(False)
            candies[i] -= extraCandies
        return result


s = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(s.kidsWithCandies(candies, extraCandies))
