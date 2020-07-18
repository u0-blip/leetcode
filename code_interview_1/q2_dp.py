class Solution:
    def numRollsToTarget(self, d, f, target) -> int:
        import numpy as np
        dp = np.ones((d, target))*-1

        dp[0, 0:f] = 1
        for i in range(d):
            for j in range(target):
                if dp[i, j] != -1:
                    continue
                dp[i,j] = 0
                # print('j', j-1, j-f)
                for k in np.arange(j-f, j):
                    # print(i, k)
                    if i-1 >= 0 and k >= 0:
                        # print(dp[i,j],dp[i-1, k])
                        # print(i, j)
                        dp[i,j] += dp[i-1, k]
        return dp[d-1, target-1]

d = 30
f = 30
target = 500

s = Solution()
print(s.numRollsToTarget(d, f, target)%(1e9+7))