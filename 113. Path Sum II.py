# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        self.sum = sum
        self.success_record = []
        self.tran_tree(root, 0, [])
        return success_record
        

    def tran_tree(self, root, sum, record):
        sum += root.val
        record.append(root.val)
        cont_val1, cont_val2 = False, False
        if root.left: cont_val1 = self.tran_tree(root.left, sum)
        if root.right: cont_val2 = self.tran_tree(root.right, sum)
        if not root.left and not root.right:
            if sum != self.sum:
                return False
            else:
                self.success_record.append(record)
                return True

        return cont_val1 or cont_val2
        