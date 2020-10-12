class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def Search(num, _Sum, oneSolution):
            if _Sum == 0 and len(oneSolution) == k:  # 找到了正确的解
                totalSolutions.append(oneSolution[:])  # 注意要切片一下。相当于复制了一遍内容。
                return

            if num == 10:  # 1~9查完了
                return

            if _Sum < 0:  # 数组和大于n了
                return

            if len(oneSolution) > k:  # 数组长度大于k了
                return

            Search(num + 1, _Sum - num, oneSolution + [num])  # 选了这个数
            Search(num + 1, _Sum, oneSolution)   # 没选择这个数

        totalSolutions = []

        Search(1, n, [])

        return totalSolutions

