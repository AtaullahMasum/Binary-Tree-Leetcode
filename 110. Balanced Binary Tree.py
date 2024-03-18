#Approach 1 Brute Force Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        left1 = self.isBalanced(root.left)
        right1 = self.isBalanced(root.right)
        if not left1 or not right1:
            return False
        return True

#Approach  2 Optimal Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkHeight(self, root):
        if not root:
            return 0
        left = self.checkHeight(root.left)
        right = self.checkHeight(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.checkHeight(root) == -1:
            return False
        else:
            return True
        