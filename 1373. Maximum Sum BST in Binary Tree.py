# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = 0
    def postorder(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0
        left_is_BST, left_min, left_max, left_sum = self.postorder(root.left)
        right_is_BST, right_min, right_max, right_sum = self.postorder(root.right)
        if left_is_BST and right_is_BST and  left_max <root.val< right_min:
            sum1 = left_sum + right_sum + root.val
            self.max_sum = max(self.max_sum, sum1)
            return True, min(left_min, root.val), max(right_max, root.val), sum1
        return False, 0, 0, 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.max_sum
        
        