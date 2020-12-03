class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        place = [0] * 101
        output = []

        for n in nums:
            place[n] += 1  # 把从0 - 100的所有数的个数都数出来了。

        lessthan = []  # 把从0 - 100的所有数的比它小的数的个数都列出来。
        temp = 0  # 其实就是刚才的place数组的累加
        for p in place:
            lessthan.append(temp)
            temp += p

        for n in nums:  # 最后对应nums把lessthan的值掏出来作为输出。
            output.append(lessthan[n])

        return output

