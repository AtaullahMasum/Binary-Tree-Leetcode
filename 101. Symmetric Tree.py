# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricHelp(self,root1, root2):
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return self.isSymmetricHelp(root1.left, root2.right) and self.isSymmetricHelp(root1.right, root2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.isSymmetricHelp(root.left, root.right)
        