# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        first = 1
        last = 1
        width = last - first +1
        queue = [(root, 0)]
        while queue:
            n = len(queue)
            first_index = queue[0][1] #first index of each level
            for i in range(n):
                node, index = queue.pop(0)
                curr_index = index - first_index # arise overflow condition so we can subtract each level node to first index node that level
                if i == 0:
                    first = curr_index
                if i == n - 1:
                    last = curr_index
                if node.left:
                    queue.append((node.left, 2*curr_index+1))
                if node.right:
                    queue.append((node.right, 2*curr_index+2))
            width = max(width, last - first + 1)
        return width