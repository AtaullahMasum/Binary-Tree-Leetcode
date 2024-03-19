# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive Solution
class Solution:
    def reversePreorder(self, root, level, result):
        if not root:
            return 
        if len(result) == level:
            result.append(root.val)
        self.reversePreorder(root.right, level+1, result)
        self.reversePreorder(root.left, level+1, result)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        self.reversePreorder(root, 0, result)
        return result
# Using Level Order Traversal 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result
        