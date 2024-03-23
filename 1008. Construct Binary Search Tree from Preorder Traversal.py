# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0
    def buildTree(self, preorder,  upper_bound):
        if self.i == len(preorder) or preorder[self.i] > upper_bound:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1  
        root.left = self.buildTree(preorder,  root.val)
        root.right = self.buildTree(preorder, upper_bound)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder, float('inf'))