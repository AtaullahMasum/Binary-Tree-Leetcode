# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from types import List, TreeNode
#DFS and BFS solution
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

#BFS and BFS Solution
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        parent[root] = None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node 
        queue =[(target, 0)]
        visited = set()
        visited.add(target)
        result = []
        while queue:
            node, dist = queue.pop(0)
            if dist == k:
                result.append(node.val)
            elif dist > k:
                break
            for child in (node.left, node.right, parent[node]):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, dist+1))
        return result

