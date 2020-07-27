import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        windows = sorted(nums[:k])
        medium = []
        for a, b in zip(nums[k:]+[0], nums):
            medium.append((windows[k//2] + windows[~(k//2)]) / 2.)
            windows.remove(b)
            bisect.insort(windows, a)
        return medium

s = Solution()
a = [1,3,-1,-3,5,3,6,7]
print(a[:-2])
print(a[3:])
k = 3
print(s.medianSlidingWindow(a, k))