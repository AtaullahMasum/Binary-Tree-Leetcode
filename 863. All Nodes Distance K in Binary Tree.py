# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from types import List, TreeNode
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        self.populateParent(root, None, parent)
        
        queue = deque([(target, 0)])
        visited = set([target])
        result = []
        
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            elif dist > k:
                break
            
            for child in (node.left, node.right, parent[node]):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, dist + 1))
        
        return result
    
    def populateParent(self, root, par, parent):
        if root:
            parent[root] = par
            self.populateParent(root.left, root, parent)
            self.populateParent(root.right, root, parent)
