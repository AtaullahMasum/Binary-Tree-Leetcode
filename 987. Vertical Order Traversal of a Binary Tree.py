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
        for _, nodes in sorted( vertical_levels.items(), key=lambda item: item[0]):#sort according to their vertical level
           result.append([val for _, val in sorted(nodes)]) #if same level has multiple node then sort ascending order 
        return result

#Using DFS (preorder traversal)
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, col, row, vertical_levels):
        if not root:
            return
        vertical_levels[col].append((row, root.val))
        self.preorder(root.left, col-1, row+1, vertical_levels)
        self.preorder(root.right, col+1, row+1, vertical_levels)
        
    def verticalTraversal(self, root):
        if not root:
            return []        
        vertical_levels = defaultdict(list)
        self.preorder(root,0,0,vertical_levels)
        result = []
        for _ , nodes in sorted(vertical_levels.items(), key = lambda item:item[0]):
            result.append([val for _, val in sorted(nodes)])
        return result