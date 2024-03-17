# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Method 1 Recursively
    def preorder(self, root, result):
        if root:
            result.append(root.val)
            self.preorder(root.left,result)
            self.preorder(root.right,result)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        #Method 2 IterativeLy
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        #self.preorder(root, result)  
        return result
