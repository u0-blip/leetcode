import numpy as np

#using sort to do it
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = np.sort(nums)
        return nums[-k]

#using heap to do it
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]

#Other person's solution, binary search, divide and conquer
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = nums.pop(random.randint(0, len(nums)-1))
        s, l = list(filter(lambda x: x<p, nums)), list(filter(lambda x: x>=p, nums))
        if len(l) == k-1 or not s and not l: return p
        if len(l) < k: return self.findKthLargest(s, k-len(l)-1)
        return self.findKthLargest(l, k) 