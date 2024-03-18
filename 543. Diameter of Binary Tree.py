#Brute force Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height (self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)
    def diameter(self, root, maximum):
        if not root:
            return 
        left = self.height(root.left)
        right = self.height(root.right)
        maximum[0] = max(maximum[0], left+right)
        self.diameter(root.left, maximum)
        self.diameter(root.right, maximum)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = [0]
        self.diameter(root, maximum)
        return maximum[0]
#Optimal Approach
class Solution:
    def height (self, root, maximum):
        if not root:
            return 0
        left = self.height(root.left, maximum)
        right = self.height(root.right, maximum)
        maximum[0] = max(maximum[0], left+right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = [0]
        self.height(root, maximum)
        return maximum[0]

