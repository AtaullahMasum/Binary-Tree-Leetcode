# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorder(self, root, result, string):
        if not root:
            return 
        if not root.left and not root.right:
            result.append(string+str(root.val))
            return 
        self.preorder(root.left, result, string+str(root.val)+"->")
        self.preorder(root.right,result, string+str(root.val)+"->")
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.preorder(root, result, "")
        return result
