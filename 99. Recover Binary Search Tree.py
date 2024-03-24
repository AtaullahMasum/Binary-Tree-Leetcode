# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first_node = None
        self.second_node = None
        self.prev_node = TreeNode(float('-inf'))
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        if self.prev_node.val > root.val:
            if not self.first_node:
                self.first_node = self.prev_node
            self.second_node = root
        self.prev_node = root
        self.inorder(root.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.inorder(root)
        self.first_node.val , self.second_node.val = self.second_node.val, self.first_node.val
        