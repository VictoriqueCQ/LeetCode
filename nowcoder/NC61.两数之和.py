#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers, target):
        # write code here
        dict = {}
        for i in range(len(numbers)):
            x = numbers[i]
            if target - x in dict:
                return [dict[target - x]+1, i+1]
            dict[x] = i
s = Solution()
print(s.twoSum([3,2,4],6))