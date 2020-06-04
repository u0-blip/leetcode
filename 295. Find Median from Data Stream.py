import numpy as np

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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()