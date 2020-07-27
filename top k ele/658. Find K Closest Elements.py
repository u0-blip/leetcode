import numpy as np
class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        arr = np.array(arr)
        index = arr.searchsorted(x)

        p1 = index - 1
        p2 = index
        if p1 <= 0:
            return arr[:k]
        elif p2 >= len(arr):
            return arr[-k:]

        closest = []

        for i in range(k):
            if p1 < 0 and p2 < len(arr):
                closest.append(arr[p2])
                p2 += 1
            elif p1 >= 0 and p2 >= len(arr):
                closest.append(arr[p1])
                p1 -= 1
            else:
                diff1 = abs(arr[p1] - x)
                diff2 = abs(arr[p2] - x)
                print('append', diff1, diff2)
                closest.append(arr[p1] if diff1 <= diff2 else arr[p2])
                if diff1<=diff2:
                    p1 -= 1
                else:
                    p2 += 1
        return sorted(closest)

                    



s = Solution()
arr = [1,2,3,4,5,6,10]
k = 4
x = 10

print(s.findClosestElements(arr, k, x))
'''
very easy, easily solved by using double pointers
'''