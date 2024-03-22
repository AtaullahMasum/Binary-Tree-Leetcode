# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, min, max):
        if not root:
            return True
        if  not min <root.val< max:
            return False
        return self.preorder(root.left, min, root.val) and self.preorder(root.right, root.val, max)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.preorder(root, float('-inf'), float('inf'))