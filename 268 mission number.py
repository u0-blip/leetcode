class Solution:
    def missingNumber(self, nums):
        i = 0

        while i < len(nums):
            num = nums[i]
            if num < len(nums) and num != i:
                nums[i], nums[num] = nums[num], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
out = 2
print(s.missingNumber(nums))