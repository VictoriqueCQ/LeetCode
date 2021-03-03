from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=sum(nums)
        if(target%2!=0):
            return False
        target//=2
        pre=[False]*(target+1)
        cur=[False]*(target+1)
        pre[0]=True
        for i in range(1,target+1):
            if(nums[0]==i):
                pre[i]=True
                break
        for i in range(1,n):
            for j in range(target+1):
                if(j>=nums[i]):
                    cur[j]= pre[j] or (pre[j-nums[i]])
                else:
                    cur[j]=pre[j]
            pre=cur[:]
        return cur[-1]

