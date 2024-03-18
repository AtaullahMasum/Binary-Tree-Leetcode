from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                current = stack.pop()
                result.append(current.val)    
                node = current.right
        return result