# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        while stack1:
            current_node = stack1.pop()
            stack2.append(current_node.val)
            if current_node.left:
                stack1.append(current_node.left)
            if current_node.right:
                stack1.append(current_node.right)
        return stack2[::-1]        