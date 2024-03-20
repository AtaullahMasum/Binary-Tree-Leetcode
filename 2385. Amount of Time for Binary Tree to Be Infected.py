# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from types import Optional, TreeNode, int
#Using BFS and BFS
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        parent[root] = None
        startnode = None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == start:
                startnode = node
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
        queue = [(startnode, 0)]
        time = 0
        visited = set([startnode])
        while queue:
            node, dist = queue.pop(0)
            time = dist
            for child in (node.left, node.right, parent[node]):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, dist+1))
        return time
#DFS and BFS
class Solution:
    def populatedParent(self, root, par, parent, startnode, start):
        if root:
            parent[root] = par
            if root.val == start:
                startnode[0] = root
            self.populatedParent(root.left, root, parent, startnode, start)
            self.populatedParent(root.right, root, parent, startnode, start)
            

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        parent[root] = None
        startnode = [None]
        self.populatedParent(root, None, parent, startnode, start)
        
        queue = [(startnode[0], 0)]
        time = 0
        visited = set([startnode[0]])
        while queue:
            node, dist = queue.pop(0)
            time = dist
            for child in (node.left, node.right, parent[node]):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, dist+1))
        return time