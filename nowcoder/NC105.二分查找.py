#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self, nums, target):
        # write code here
        a, b = 0, len(nums) - 1
        while a <= b:
            c = (a + b) // 2
            t = nums[c]
            if target == t:
                if a == b:
                    return c
                else:
                    b = c
            elif target < t:
                b = c - 1
            else:
                a = c + 1
        return -1

s = Solution()
print(s.search([1,2,4,4,5],4))