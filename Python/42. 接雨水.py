class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        ans = 0
        length = len(height)
        left_max = [0]*length
        right_max = [0]*length
        left_max[0] = height[0]
        right_max[length-1] = height[length-1]
        for i in range(1,length):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(length-2,-1,-1):
            right_max[i] = max(height[i],right_max[i+1])
        for i in range(1,length-1):
            ans+=min(left_max[i],right_max[i])-height[i]
        return ans