class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn)
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)
            return max(scoreStart * turn, scoreEnd * turn) * turn

        return total(0, len(nums) - 1, 1) >= 0

class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0

