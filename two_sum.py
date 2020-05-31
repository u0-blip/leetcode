nums = [3,2,3]

target = 6
from itertools import islice
import numpy as np

args = np.argsort(nums)
nums = np.sort(nums)
#search solution

for i in range(len(nums)):
    value_to_look = target - nums[i]
    a = np.searchsorted(nums[i+1:], value_to_look)
    if a+i+1 >= len(nums):
        if nums[a+i] == value_to_look:
            print(sorted([args[i], args[a+i+1]]))
    else:
        if nums[a+i+1] == value_to_look:
            print(sorted([args[i], args[a+i+1]]))
        