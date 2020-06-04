class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        root = []
        sol = [[]]
        for num in nums:
            copy_sol = deepcopy(sol)
            for i in range(len(copy_sol)):
                copy_sol[i].append(num)
            sol = sol+copy_sol
        return sol
        
# better solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets