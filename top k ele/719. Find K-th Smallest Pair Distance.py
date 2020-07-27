import numpy as np


class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        ''' this method uses trial and error algorith binary search to find the kth smallest pair '''
        nums.sort()
        nums = np.array(nums)
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l+r)//2
            cnt = 0
            index = 0
            for i, ele in enumerate(nums):
                # index = nums.searchsorted(ele+mid)
                while index < len(nums) and nums[index] <= ele + mid:
                    index += 1
                # print('index', index)
                cnt += index - i - 1
            if cnt < k:
                l = mid + 1
            else:
                r = mid 
        return l

s = Solution()
nums = [1, 3, 6, 10, 12, 17]

k = 1
print(s.smallestDistancePair(nums, k))

''' 
what kind of pattern is this question? 
kth element question
the intuition behind solving this question is that: 
1. the search space for the answer is between the largest pair difference and 0.
2. the way to verify a solution is to go through the array and count how many pairs are smaller than the current solution.
to go through the array and find the index where the number is smaller than the current index + solution. 
the resulting count is how many pairs at current index is smaller than the current solution.
3. due to the fact that count function is monotonic, binary search can be performed to find the optimal solution. 
The count is then used to compare with k to deduct which side of the number array to keep. (binary search)
'''