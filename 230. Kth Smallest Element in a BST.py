# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        
    def inorder(self, root, k, result):
        if not root:
            return 
        self.inorder(root.left, k, result)
        self.count += 1
        if self.count == k:
            result[0] = root.val
            return 
        self.inorder(root.right, k, result)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [0]
        self.inorder(root, k,result)
        return result[0]
