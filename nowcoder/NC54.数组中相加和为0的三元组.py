#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self, num):
        # write code here
        res = []
        n = len(num)
        if n < 3:
            return []  # 如果num中元素少于三个
        num.sort()  # num中元素由小到大排序
        for i in range(n - 2):
            if num[i] > 0:
                break  # 最小值为正数，不构成三元组
            if num[i] == num[i - 1] and i > 0:
                continue
            l = i + 1  # 双指针 左边,变大
            r = n - 1  # 右边，变小
            while l < r:
                s = num[i] + num[l] + num[r]
                if s == 0:
                    res.append([num[i], num[l], num[r]])
                    l += 1  # 如果和为0，i不变的情况下，探寻所有l和r的可能组合
                    r -= 1
                    while l < r and num[l] == num[l - 1]:  # 两个数相同，l+1
                        l += 1
                    while l < r and num[r] == num[r + 1]:  # 两个数相同，r-1
                        r -= 1
                elif s < 0:  # s<0，不够，r已经是最大的数，增加l的值
                    l += 1
                else:  # s>0,太大，l已经是最小的数，减小r的值
                    r -= 1
        return res
