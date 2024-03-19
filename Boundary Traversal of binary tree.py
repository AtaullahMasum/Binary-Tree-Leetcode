'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isLeaf(self, node ):
        if not node.left  and not node.right:
            return True
        return False
    def leftBoundary(self, root, result):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                result.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
    def leafNode(self, root, result):
        if self.isLeaf(root):
            result.append(root.data)
            return
        if root.left:
            self.leafNode(root.left, result)
        if root.right:
            self.leafNode(root.right, result)
    
    def rightBoundary(self, root, result):
        curr = root.right
        subresult = []
        while curr:
            if not self.isLeaf(curr):
                subresult.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        result.extend(subresult[::-1])
    def printBoundaryView(self, root):
        # Code here
        if not root:
            return []
        result = []
        if not self.isLeaf(root):
            result.append(root.data)
        self.leftBoundary(root, result)
        self.leafNode(root, result)
        self.rightBoundary(root, result)
        return result
        
