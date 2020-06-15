import numpy as np


class Solution:
    def canPartition(self, nums):
        sum = np.sum(nums)
        if ((sum % 2) == 1):
            return False
        sum /= 2
        sum = int(sum)
        n = len(nums)
        dp = np.zeros((int(n+1), int(sum)+1)).astype(np.bool)
        
        dp[0, 0] = True
        
        for i in range(n+1):
            dp[i, 0] = True
        
        for j in range(sum+1):
            dp[0, j] = False
        
        
        for i in range(n+1):
            for j in range(sum+1): 
                dp[i, j] = dp[i-1, j]
                if (j >= nums[i-1]) :
                    dp[i, j] = (dp[i, j] or dp[i-1, j-nums[i-1]])
                
            
        return dp[n, sum]
    

s = Solution()
a = [1,2,3,5, 3]
print(s.canPartition(a))