from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []        
        vertical_levels = defaultdict(list)
        queue = [(0, 0, root)]
        while queue:
            col, row, node = queue.pop(0)
            vertical_levels[col].append((row, node.val))
            if node.left:
                queue.append((col - 1, row + 1, node.left))
            if node.right:
                queue.append((col + 1, row + 1, node.right))        
        result = []
        for _, nodes in sorted( vertical_levels.items(), key=lambda item: item[0]):
           result.append([val for _, val in sorted(nodes)])  
        return result