# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def changeTree(self, root):
        if not root:
            return
        children_sum = 0
        if root.left:
            children_sum += root.left.val
        if root.right:
            children_sum += root.right.val
        if children_sum > root.val:
            root.val = children_sum
        else:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val
        self.changeTree(root.left)
        self.changeTree(root.right)
        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
        if root.left or root.right:
            root.val = total
            
    
    
