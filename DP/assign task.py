import numpy as np
import math
import itertools
cost = [[1,2,3,4], [2,3,4,5], [4,5,6,7], [7,8,8,9]]

def assign(N,  cost):
    assignment = [0 for i in range(N)]
    for i in range(N):
        assignment[i] = i            #assigning task i to person i
    res = np.inf
    for i, assignment in enumerate(itertools.permutations(assignment)):
        total_cost = 0
        for i in range(N):
            total_cost = total_cost + cost[i][assignment[i]]
        res = min(res, total_cost)
    return res

print(assign(4, cost))