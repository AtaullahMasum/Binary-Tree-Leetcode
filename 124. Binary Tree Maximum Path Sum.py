# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxPathSum(self, root, maximum):
        if not root:
            return 0
        left = max(0, self.findMaxPathSum(root.left, maximum))
        right = max(0, self.findMaxPathSum(root.right, maximum))
        maximum[0] = max(maximum[0], root.val+ left+right)
        return root.val + max(left, right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = [float('-inf')]
        self.findMaxPathSum(root, maximum)
        return maximum[0]
        