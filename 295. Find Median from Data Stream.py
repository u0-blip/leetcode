import numpy as np

#brute force, searchsorted solution
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.kept = np.array([])

    def addNum(self, num: int) -> None:
        index = np.searchsorted(self.kept, num)
        self.kept= np.insert(self.kept, index, num)

    def findMedian(self) -> float:
        l = len(self.kept)
        if l%2 == 0:
            return (self.kept[int(l/2)-1]+self.kept[int(l/2)])/2
        else:
            return self.kept[int(l/2)]


from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both heaps will have equal number of elements or max-heap will have one more element
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # we have even number of elements, take the average of middle two elements
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        # we have odd number of elements, the first element in max-heap is the median element
        return -float(self.max_heap[0])
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()