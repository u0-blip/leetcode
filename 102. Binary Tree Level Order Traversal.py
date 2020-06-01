# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if (root == None):
            return root
        all_l = [[root]]
        l = []
        if root.left: l.append(root.left)
        if root.right: l.append(root.right)
        all_l.append(l)
        
        while(len(all_l[-1]) > 0):
            l = []
            for i in range(len(all_l[-1])):
                root = all_l[-1][i]
                if root.left: l.append(root.left)
                if root.right: l.append(root.right)
            all_l.append(l)
        
        all_v = []
        for i in range(len(all_l)):
            if len(all_l[i]) == 0:
                continue
            v = []
            for j in range(len(all_l[i])):
                v.append(all_l[i][j].val)
            all_v.append(v)
        return all_v
        