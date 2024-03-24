# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        seen = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            complement = k - node.val
            if complement in seen:
                return True
            seen.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
#Using Binary Search Tree Iterator
class Solution:
    class BSTIterator:

        def __init__(self, root: Optional[TreeNode], reverse):
            self.stack = []
            self.reverse = reverse
            self.pushAll(root)
        def next(self) -> int:
            node = self.stack.pop()
            if not self.reverse:
                self.pushAll(node.right)
            else:
                self.pushAll(node.left)
            return node.val

        def hasNext(self) -> bool:
            return len(self.stack) > 0
        def pushAll(self, node):
            while node:
                self.stack.append(node)
                if not self.reverse:
                    node = node.left
                else:
                    node = node.right
                    
            

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root :
            return False
        l= Solution.BSTIterator(root, False)
        r= Solution.BSTIterator(root, True)
        i = l.next()
        j = r.next()
        while i < j:
            if i + j == k:
                return True
            if i + j < k:
                i= l.next()
            else:
                j = r.next()
        return False