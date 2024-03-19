#User function Template for python3
from collections import defaultdict

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        result = []
        vertical_levels = defaultdict(int)
        queue = [(root, 0)]
        while queue:
            node, vertical_line = queue.pop(0)
            if vertical_line not in vertical_levels:
                vertical_levels[vertical_line] = node.data
            if node.left:
                queue.append((node.left, vertical_line - 1))
            if node.right:
                queue.append((node.right, vertical_line + 1))
        for x in sorted( vertical_levels):
            result.append(vertical_levels[x])
        return result
