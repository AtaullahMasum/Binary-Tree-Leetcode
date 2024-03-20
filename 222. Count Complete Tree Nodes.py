# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftheight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
    def rightheight(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lefth = self.leftheight(root)
        righth = self.rightheight(root)
        if lefth == righth:
            return 2**lefth- 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)